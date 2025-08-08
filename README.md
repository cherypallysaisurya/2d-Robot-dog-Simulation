# 🤖 Robot Behavior Simulator - Quick Guide for Educators

## 📦 **Installation**
```bash
pip install --index-url https://test.pypi.org/simple/ robot-behavior-simulator
🎯 What It Does
Educational Python package for teaching programming through visual robot simulation. Students write code to move a triangle robot through a grid world, creating red trails and navigating obstacles.

🚀 Quick Test
bash
Copy
Edit
robot-demo  # Run built-in demonstration
📝 Basic Student Code
python
Copy
Edit
from robot_behavior import create_robot_program

# Create 5x5 world, robot starts at (0,0)
program = create_robot_program(5, 5, 0, 0)

# Add walls
program.add_wall(2, 2)
program.add_wall(3, 2)

# Move robot
program.robot.move('right')
program.robot.move('right')
program.robot.move('up')
program.robot.move('up')

# Show visual result
program.start()
🎓 Educational Benefits
Visual Learning: Immediate feedback with animated robot and red trail

Spatial Reasoning: Grid-based coordinate system

Problem Solving: Navigate mazes and obstacles

Programming Concepts: Sequencing, loops, conditionals

🖥️ Platform Support
✅ Windows ✅ macOS ✅ Linux

📊 Visual Output
Students see:

Blue triangle robot moving on grid

Red trail showing complete path

Black walls as obstacles

Interactive GUI with reset/close buttons

🎯 Classroom Activities
Draw shapes with robot movements

Solve maze challenges

Create geometric patterns

Coordinate-based treasure hunts

📞 Support
Package: https://test.pypi.org/project/robot-behavior-simulator/

GitHub: https://github.com/cherypallysaisurya/2d-Robot-dog-Simulation










Ask ChatGPT
