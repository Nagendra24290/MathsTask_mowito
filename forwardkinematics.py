import numpy as np

def forward_kinematics(j1, j2, j3, j4, L=1.0):
    # Convert to radians
    j1 = np.radians(j1)
    j2 = np.radians(j2)
    j3 = np.radians(j3)
    j4 = np.radians(j4)

    # Compute cumulative joint angles
    a1 = j2
    a2 = j2 + j3
    a3 = j2 + j3 + j4

    # Forward kinematics equations
    x = np.cos(j1) * (L*np.cos(a1) + L*np.cos(a2) + L*np.cos(a3))
    y = np.sin(j1) * (L*np.cos(a1) + L*np.cos(a2) + L*np.cos(a3))
    z = L*np.sin(a1) + L*np.sin(a2) + L*np.sin(a3)

    return x, y, z

# Example usage:
print(forward_kinematics(30, 45, -20, 10))
