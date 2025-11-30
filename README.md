🔢 Robotics Mathematics Tasks – FK + Quaternion Conversion
🧮 Mowito Internship – Robotics Math Module






This repository contains two core robotics mathematics tasks implemented in Python:
✔ Euler ↔ Quaternion Conversion
✔ 2-DOF Forward Kinematics with Visualization

These concepts form the foundation of robot motion representation and kinematic analysis.

📌 Project Structure
math_task/
│
├── conversions/
│   ├── euler_to_quaternion.py
│   ├── quaternion_to_euler.py
│   └── conversion_test.py
│
└── forward_kinematics/
    ├── fk_math.py
    ├── fk_pygame_sim.py
    └── media/ (add simulation screenshots)

🧩 PART A — Euler ↔ Quaternion Conversion
🎯 Objective

Convert between:

From	To
Roll, Pitch, Yaw (Euler)	Quaternion
Quaternion	Roll, Pitch, Yaw (Euler)

⭐ Supports angles in degrees
⭐ Includes unit-tested sample values

📘 Mathematical Formulation

Quaternion:

qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)

📸 Sample Output
Euler Input	Quaternion Output
(30°, 0°, 60°)	(0.20, 0.34, 0.56, 0.73)

➡ Insert screenshot: media/quaternion_terminal.png

🧩 PART B — Forward Kinematics + Pygame Visualization
🎯 Objective

Compute 2-Link Robotic Arm End-Effector Position:

x = L1*cos(θ1) + L2*cos(θ1 + θ2)
y = L1*sin(θ1) + L2*sin(θ1 + θ2)


✔ Real-time motion visualization using Pygame
✔ Keyboard-controlled joint angles
✔ End-Effector coordinates displayed live

🎮 Simulation Preview
Mode	Description
Normal	Live joint manipulation + arm tracking

➡ Insert screenshots in media/ folder before uploading

🔧 Installation
pip install pygame numpy

▶️ Running the Applications
Angle Conversions:
python3 conversions/conversion_test.py

FK Simulation:
python3 forward_kinematics/fk_pygame_sim.py

📊 Example Console Output
Angle1: 45°, Angle2: 20°
End Effector Position → X: 95.2, Y: 70.8

🚀 Skills Demonstrated
Topic	Applied In
Euler Angles & Rotation	Quaternion Conversion
Spatial Orientation	FK Simulation
Trigonometry	Arm link transformations
Scientific Computing	Numpy & Math
Real-Time UI	Pygame Graphics
👨‍💻 Author

Daggupati Nagendra
Robotics & Automation Engineer
Mowito Internship — Robotics Math Task

📧 Email: daggupatinagendra24@gmail.com

🔗 Portfolio (add when ready)
