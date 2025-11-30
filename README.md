# 🔢 Robotics Mathematics Task – Quaternion Conversion + Forward Kinematics

This repository includes essential robotics mathematics concepts implemented in Python as part of my **Mowito Internship**:

✔ Euler ↔ Quaternion Angle Conversion  
✔ 2-DOF Robotic Arm Forward Kinematics & Visualization  

These modules are fundamental for robot motion orientation and spatial kinematics.

---

## 📂 Folder Structure


math_task/
├── conversions/
│ ├── euler_to_quaternion.py
│ ├── quaternion_to_euler.py
│ └── conversion_test.py
│
└── forward_kinematics/
├── fk_math.py
├── fk_pygame_sim.py
└── media/


---

## 🧩 PART A — Euler ↔ Quaternion Conversion

### 🎯 Objective
Convert between:
- **Roll, Pitch, Yaw (Euler Angles) → Quaternion**
- **Quaternion → Euler Angles**

### 📌 Features
- Supports degree inputs
- Tested with sample values

### 🔢 Example Output


Euler: (30°, 0°, 60°)
Quaternion: (0.20, 0.34, 0.56, 0.73)


📸 Screenshot location:  
`conversions/media/quaternion_terminal.png`

---

## 🧩 PART B — 2-DOF Forward Kinematics Visualization

### 🎯 Objective
Compute end-effector position using:


x = L1cos(θ1) + L2cos(θ1 + θ2)
y = L1sin(θ1) + L2sin(θ1 + θ2)


### 🎮 Features
- Real-time animation using **Pygame**
- Keyboard control for joints
- Displays end-effector coordinates live

📸 Add UI screenshots here:  
`forward_kinematics/media/`

---

## 🔧 Installation
```bash
pip install numpy pygame

▶️ Run Instructions
Quaternion Conversion Test
python3 conversions/conversion_test.py

FK Simulation
python3 forward_kinematics/fk_pygame_sim.py

📊 Example Console Output
Angle1: 45°, Angle2: 20°
End Effector Position → X: 95.2, Y: 70.8

🧠 Skills Demonstrated
Concept	Usage
Rotation Mathematics	Quaternion Conversion
Trigonometry	FK Computation
Spatial Orientation	Robotic Arm Positioning
Real-Time Visualization	Pygame
Python Math & Scientific Libraries	Numpy & Math
👨‍💻 Author

Daggupati Nagendra
Robotics & Automation Engineer
📧 Email: daggupatinagendra24@gmail.com

⭐ If you like this project, please consider giving the repo a star!


---

### ✨ Done!  
