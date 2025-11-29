🔢 Math Robotics Task – FK + Quaternion Conversion
🧮 Robotics Mathematics Project – Mowito Internship






📘 Project Summary

This repository contains two core robotics mathematics modules:

Task	Description	Status
Angle Conversions	Euler ↔ Quaternion conversions using Python math	✔
Forward Kinematics	2-DOF robotic arm arm visualization	✔

These mathematical fundamentals are essential for robotics motion representation and manipulation.

🧩 PART A – Euler ↔ Quaternion Conversion
🎯 Objective

Convert between:

Roll, Pitch, Yaw → Quaternion

Quaternion → Roll, Pitch, Yaw

Using equations:

qx = ...
qy = ...
qz = ...
qw = ...


📁 Folder Structure

math_task/
└── conversions/
    ├── euler_to_quaternion.py
    ├── quaternion_to_euler.py
    └── conversion_test.py


📌 Supports angles in degrees
📌 Unit-tested sample values

📸 Output Sample
Euler Input	Quaternion Result
(30°, 0°, 60°)	(0.20, 0.34, 0.56, 0.73)

➡ Add screenshot here: media/quaternion_terminal.png

🧩 PART B – Forward Kinematics with Visualization
🎯 Objective

2-Link Robotic Arm FK:

x = L1*cos(θ1) + L2*cos(θ1 + θ2)
y = L1*sin(θ1) + L2*sin(θ1 + θ2)


📁 Folder Structure

math_task/
└── forward_kinematics/
    ├── fk_math.py            # End-effector compute
    ├── fk_pygame_sim.py      # Graphical animation
    └── README.md (this file)


📌 Real-time visualization using Pygame
📌 Keyboard control for joint angles
📌 End-effector coordinate display

📸 Simulation UI
Color Mode	Joint Motion Preview

	

(Add screenshots into media/ folder before uploading ✓)

🔧 Installation
pip install pygame numpy

▶️ Run Programs
Angle Conversions
python3 conversions/conversion_test.py

FK Simulation
python3 forward_kinematics/fk_pygame_sim.py

📊 Example Console Output
Angle1: 45°, Angle2: 20°
End Effector Position → X: 95.2, Y: 70.8

🧠 Skills Demonstrated
Topic	Applied In
Euler Angles & Rotation	Quaternion Conversion
Spatial Orientation	FK Simulation
Trigonometry	Link Transformations
Scientific Computing	Python Math Libraries
Real-Time Visualization	Pygame
🧑‍💻 Author

Daggupati Nagendra
Robotics & Automation Engineer
Mowito Internship — Math Robotics Task

📧 Email: daggupatinagendra24@gmail.com
