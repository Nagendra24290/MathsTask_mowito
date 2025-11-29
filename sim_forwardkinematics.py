import pygame
import numpy as np
import sys

# ------------- Forward Kinematics ---------------- #

def forward_kinematics(j1, j2, j3, j4, L=1.0):
    """
    Forward kinematics for a 4-DOF arm.
    j1, j2, j3, j4 are in degrees.
    Returns (x, y, z) of end-effector in meters.
    """

    # Convert to radians
    j1_r = np.radians(j1)
    j2_r = np.radians(j2)
    j3_r = np.radians(j3)
    j4_r = np.radians(j4)

    # Cumulative angles for joints 2,3,4
    a1 = j2_r
    a2 = j2_r + j3_r
    a3 = j2_r + j3_r + j4_r

    # Planar reach in the x-y plane (relative to base rotation)
    reach = L * np.cos(a1) + L * np.cos(a2) + L * np.cos(a3)

    # 3D FK
    x = np.cos(j1_r) * reach
    y = np.sin(j1_r) * reach
    z = L * np.sin(a1) + L * np.sin(a2) + L * np.sin(a3)

    return x, y, z


def compute_joint_positions_2d(j2, j3, j4, L=1.0, scale=150, base=(400, 300)):
    """
    For visualization in 2D (side view: x–z plane).
    We ignore j1 visually (only used in 3D FK above).
    Returns list of points: [base, joint1, joint2, joint3, end_effector]
    in screen coordinates for Pygame.
    """
    j2_r = np.radians(j2)
    j3_r = np.radians(j3)
    j4_r = np.radians(j4)

    a1 = j2_r
    a2 = j2_r + j3_r
    a3 = j2_r + j3_r + j4_r

    bx, by = base

    # Joint 1 (end of link 1)
    x1 = bx + L * np.cos(a1) * scale
    y1 = by - L * np.sin(a1) * scale  # minus because screen y grows downward

    # Joint 2 (end of link 2)
    x2 = x1 + L * np.cos(a2) * scale
    y2 = y1 - L * np.sin(a2) * scale

    # Joint 3 (end of link 3)
    x3 = x2 + L * np.cos(a3) * scale
    y3 = y2 - L * np.sin(a3) * scale

    # End effector (link 4)
    x4 = x3 + L * np.cos(a3) * scale
    y4 = y3 - L * np.sin(a3) * scale

    return [(bx, by), (x1, y1), (x2, y2), (x3, y3), (x4, y4)]


# ------------- Pygame Visualization ------------- #

def main():
    pygame.init()

    # Window setup
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("4-DOF Robot Arm - Forward Kinematics (Pygame)")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 18)

    # Robot parameters
    L = 1.0          # link length in meters
    scale = 150      # pixels per meter
    base = (WIDTH // 2, HEIGHT // 2 + 100)

    # Joint angles in degrees (initial)
    j1 = 0.0
    j2 = 0.0
    j3 = 0.0
    j4 = 0.0

    angle_step = 2.0  # degrees per key press

    running = True
    while running:
        clock.tick(60)  # 60 FPS

        # ----- Event Handling ----- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key handling (continuous)
        keys = pygame.key.get_pressed()

        # Joint 1 (base rotation around Z)
        if keys[pygame.K_q]:
            j1 += angle_step
        if keys[pygame.K_a]:
            j1 -= angle_step

        # Joint 2
        if keys[pygame.K_w]:
            j2 += angle_step
        if keys[pygame.K_s]:
            j2 -= angle_step

        # Joint 3
        if keys[pygame.K_e]:
            j3 += angle_step
        if keys[pygame.K_d]:
            j3 -= angle_step

        # Joint 4
        if keys[pygame.K_r]:
            j4 += angle_step
        if keys[pygame.K_f]:
            j4 -= angle_step

        if keys[pygame.K_ESCAPE]:
            running = False

        # ----- Compute FK and joint positions ----- #
        x, y, z = forward_kinematics(j1, j2, j3, j4, L=L)
        joints = compute_joint_positions_2d(j2, j3, j4, L=L, scale=scale, base=base)

        # ----- Draw ----- #
        screen.fill((0, 0, 0))  # clear screen

        # Draw base
        pygame.draw.circle(screen, (200, 200, 200), base, 8)

        # Draw links
        for i in range(len(joints) - 1):
            pygame.draw.line(screen, (255, 255, 255),
                             joints[i], joints[i + 1], 4)
            pygame.draw.circle(screen, (0, 255, 0),
                               (int(joints[i + 1][0]), int(joints[i + 1][1])), 6)

        # ----- Text info ----- #
        # Angles
        text_angles = [
            f"j1: {j1:6.1f} deg (Q/A)",
            f"j2: {j2:6.1f} deg (W/S)",
            f"j3: {j3:6.1f} deg (E/D)",
            f"j4: {j4:6.1f} deg (R/F)",
        ]

        # End-effector position
        text_pos = [
            f"End-effector (FK):",
            f"x = {x:5.3f} m",
            f"y = {y:5.3f} m",
            f"z = {z:5.3f} m",
        ]

        # Render angle text
        y_offset = 10
        for line in text_angles:
            img = font.render(line, True, (255, 255, 255))
            screen.blit(img, (10, y_offset))
            y_offset += 22

        # Render position text
        y_offset += 10
        for line in text_pos:
            img = font.render(line, True, (255, 255, 0))
            screen.blit(img, (10, y_offset))
            y_offset += 22

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
