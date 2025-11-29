import math

# ------------- Utility functions ------------- #

def _deg2rad(angle_deg):
    return angle_deg * math.pi / 180.0

def _rad2deg(angle_rad):
    return angle_rad * 180.0 / math.pi

def _normalize_quaternion(w, x, y, z, eps=1e-10):
    """Normalize quaternion to unit length. Handle zero-length safely."""
    norm = math.sqrt(w*w + x*x + y*y + z*z)
    if norm < eps:
        # Degenerate quaternion – return identity rotation
        return 1.0, 0.0, 0.0, 0.0
    return w / norm, x / norm, y / norm, z / norm


# ------------- Euler → Quaternion ------------- #
# Convention: ZYX (yaw–pitch–roll)
# roll  = rotation about X
# pitch = rotation about Y
# yaw   = rotation about Z

def euler_to_quaternion(roll, pitch, yaw, degrees=False):
    """
    Convert Euler angles to quaternion.

    Parameters
    ----------
    roll  : float  (rotation about X)
    pitch : float  (rotation about Y)
    yaw   : float  (rotation about Z)
    degrees : bool
        If True, input angles are in degrees; internally converted to radians.

    Returns
    -------
    (w, x, y, z) : tuple of floats
        Unit quaternion representing the same orientation.
    """
    if degrees:
        roll  = _deg2rad(roll)
        pitch = _deg2rad(pitch)
        yaw   = _deg2rad(yaw)

    cr = math.cos(roll  * 0.5)
    sr = math.sin(roll  * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cy = math.cos(yaw   * 0.5)
    sy = math.sin(yaw   * 0.5)

    # ZYX order (yaw, pitch, roll)
    w = cr*cp*cy + sr*sp*sy
    x = sr*cp*cy - cr*sp*sy
    y = cr*sp*cy + sr*cp*sy
    z = cr*cp*sy - sr*sp*cy

    return _normalize_quaternion(w, x, y, z)


# ------------- Quaternion → Euler ------------- #

def quaternion_to_euler(w, x, y, z, degrees=False):
    """
    Convert quaternion to Euler angles (ZYX: yaw–pitch–roll).

    Parameters
    ----------
    w, x, y, z : float
        Quaternion components. They will be normalized internally.
    degrees : bool
        If True, output angles are in degrees.

    Returns
    -------
    (roll, pitch, yaw) : tuple of floats
        Euler angles in radians or degrees (if degrees=True).
    """
    # Normalize to be safe
    w, x, y, z = _normalize_quaternion(w, x, y, z)

    # roll (x-axis rotation)
    sinr_cosp = 2.0 * (w*x + y*z)
    cosr_cosp = 1.0 - 2.0 * (x*x + y*y)
    roll = math.atan2(sinr_cosp, cosr_cosp)

    # pitch (y-axis rotation)
    sinp = 2.0 * (w*y - z*x)

    # Numerical safety / gimbal lock handling
    if abs(sinp) >= 1.0:
        # Use 90 degrees with sign of sinp
        pitch = math.copysign(math.pi / 2.0, sinp)
    else:
        pitch = math.asin(sinp)

    # yaw (z-axis rotation)
    siny_cosp = 2.0 * (w*z + x*y)
    cosy_cosp = 1.0 - 2.0 * (y*y + z*z)
    yaw = math.atan2(siny_cosp, cosy_cosp)

    if degrees:
        return _rad2deg(roll), _rad2deg(pitch), _rad2deg(yaw)
    else:
        return roll, pitch, yaw


# ------------- Test / Demo ------------- #

if __name__ == "__main__":
    # Example Euler angles
    roll_deg  = 30.0
    pitch_deg = 45.0
    yaw_deg   = 60.0

    print("Input Euler (deg):")
    print(f"  roll  = {roll_deg}")
    print(f"  pitch = {pitch_deg}")
    print(f"  yaw   = {yaw_deg}")

    # Euler → Quaternion
    q = euler_to_quaternion(roll_deg, pitch_deg, yaw_deg, degrees=True)
    w, x, y, z = q
    print("\nQuaternion (w, x, y, z):")
    print(f"  w = {w:.6f}")
    print(f"  x = {x:.6f}")
    print(f"  y = {y:.6f}")
    print(f"  z = {z:.6f}")

    # Quaternion → Euler (round-trip)
    r2, p2, y2 = quaternion_to_euler(w, x, y, z, degrees=True)
    print("\nRecovered Euler from quaternion (deg):")
    print(f"  roll  = {r2:.6f}")
    print(f"  pitch = {p2:.6f}")
    print(f"  yaw   = {y2:.6f}")

    # Edge case check: near gimbal lock (pitch ~ 90°)
    print("\nGimbal-lock edge case test (pitch ≈ 90°):")
    roll_g  = 10.0
    pitch_g = 89.999
    yaw_g   = 20.0

    w_g, x_g, y_g, z_g = euler_to_quaternion(roll_g, pitch_g, yaw_g, degrees=True)
    r_g, p_g, y_g2 = quaternion_to_euler(w_g, x_g, y_g, z_g, degrees=True)

    print(f"  Input  : roll={roll_g}, pitch={pitch_g}, yaw={yaw_g}")
    print(f"  Output : roll={r_g:.6f}, pitch={p_g:.6f}, yaw={y_g2:.6f}")
