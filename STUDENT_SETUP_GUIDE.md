# 🤖 Robot Simulation Framework - Student Setup Guide

Welcome! This guide will help you get the robot simulation running on your computer in just a few minutes.

## 🚀 Quick Start (3 Steps)

### Step 1: Download the Project
```bash
# If using Git:
git clone [YOUR_GITHUB_URL]
cd Robot-behavior

# OR download ZIP file from GitHub and extract it
```

### Step 2: Install the Package
```bash
# Install in development mode (recommended)
pip install -e .

# OR install dependencies only
pip install numpy
```

### Step 3: Run the Examples
```bash
cd examples
python student_example.py
```

That's it! You should see robot simulations opening in separate windows.

---

## 🖥️ System Requirements

### ✅ What You Need:
- **Python 3.7+** (comes with Tkinter built-in)
- **pip** (Python package installer)
- **Any operating system** (Windows, Mac, Linux)

### ✅ What's Already Included:
- **Tkinter** - GUI library (built into Python)
- **All robot logic** - No extra downloads needed

### ❌ What You DON'T Need:
- Complex game engines
- ROS (Robot Operating System)
- pygame or other graphics libraries
- Virtual environments (optional but recommended)

---

## 🎯 For Different Platforms

### Windows
```cmd
# Check Python version
python --version

# Install package
pip install -e .

# Run examples
cd examples
python student_example.py
```

### Mac/Linux
```bash
# Check Python version
python3 --version

# Install package
pip3 install -e .

# Run examples
cd examples
python3 student_example.py
```

### Online IDEs (Replit, Google Colab)
See the "Online IDE Setup" section below.

---

## 🧑‍💻 For Students: How to Create Your Own Robot Behaviors

### Option 1: Modify the Example File
1. Open `examples/student_example.py`
2. Change the numbers in existing functions:
   ```python
   run_prime_bot([2, 3, 5, 7, 11, 13, 17, 19])  # More primes
   run_spiral_bot(8)  # Bigger spiral
   ```

### Option 2: Create Your Own File
1. Create a new file: `examples/my_robot.py`
2. Copy this template:
   ```python
   from robot_behavior.behaviors.api import RobotProgram
   
   # Create your robot
   program = RobotProgram()
   
   # Add walls
   program.add_wall(3, 3)
   program.add_wall(4, 4)
   
   # Your custom logic here
   for i in range(10):
       if i % 3 == 0:
           program.robot.turn_left()
       else:
           program.robot.move_forward()
   
   # Start the simulation
   program.simulator.root.after(3000, lambda: program.simulator.close())
   program.start()
   ```

### Option 3: Create New Behaviors (Advanced)
1. Open `robot_behavior/behaviors/basic.py`
2. Add your function:
   ```python
   def my_custom_behavior(robot: Robot, parameter):
       """Your behavior description"""
       for i in range(parameter):
           # Your logic here
           robot.move_forward()
           robot.turn_right()
   ```
3. Use it in your code:
   ```python
   from robot_behavior.behaviors.basic import my_custom_behavior
   program.run_behavior(my_custom_behavior, 5)
   ```

---

## 🌐 Online IDE Setup

### Replit.com
1. Create new Python Repl
2. Upload all project files
3. In Shell tab: `pip install -e .`
4. Run: `python examples/student_example.py`
5. ⚠️ **Note**: Tkinter may have limited support on Replit

### Google Colab
1. Upload project as ZIP
2. Extract files
3. Install: `!pip install -e .`
4. ⚠️ **Note**: Tkinter doesn't work in Colab - see web version below

### CodeSpaces / Gitpod
1. Fork the repository
2. Open in CodeSpaces
3. Tkinter should work with X11 forwarding

---

## 🔧 Troubleshooting

### "No module named 'robot_behavior'"
```bash
# Make sure you're in the project root directory
cd Robot-behavior
pip install -e .
```

### "No module named 'tkinter'"
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# Mac (if using Homebrew)
brew install python-tk
```

### "Permission denied"
```bash
# Use --user flag
pip install -e . --user
```

### Robot window doesn't appear
- Check if you're running in a headless environment
- Make sure you have a display/screen available
- Try running with `python -m examples.student_example`

---

## 📁 Safe Editing Guidelines

### ✅ SAFE TO EDIT:
- `examples/student_example.py` - Your playground
- `examples/my_custom_file.py` - Create new files here
- `robot_behavior/behaviors/basic.py` - Add new behaviors

### ⚠️ EDIT CAREFULLY:
- `robot_behavior/behaviors/api.py` - Student interface functions

### ❌ DON'T TOUCH:
- `robot_behavior/core/robot.py` - Core robot logic
- `robot_behavior/simulator/simulator.py` - GUI code
- `setup.py` - Package configuration

---

## 🎓 Learning Path

### Beginner (10 minutes)
1. Run `python examples/student_example.py`
2. Change numbers in `run_prime_bot([2, 3, 4, 5])`
3. Modify wall positions in custom behavior

### Intermediate (30 minutes)
1. Create your own behavior file
2. Add custom movement patterns
3. Experiment with different grid sizes

### Advanced (1 hour+)
1. Create new behavior functions in `basic.py`
2. Add new robot capabilities
3. Modify visual elements

---

## 📤 Sharing Your Work

### Share Your Behavior File:
```python
# Save as: my_awesome_robot.py
from robot_behavior.behaviors.api import RobotProgram

def my_fibonacci_robot():
    program = RobotProgram(width=15, height=15)
    
    # Fibonacci sequence robot
    a, b = 1, 1
    for _ in range(10):
        for _ in range(a):
            program.robot.move_forward()
        program.robot.turn_right()
        a, b = b, a + b
    
    program.start()

if __name__ == "__main__":
    my_fibonacci_robot()
```

### Create a GitHub Repository:
1. Fork this project
2. Add your custom behaviors
3. Share the link with friends!

---

## 🆘 Getting Help

1. **Check the logs**: Look at `robot_movement.log`
2. **Read error messages**: They usually tell you what's wrong
3. **Start simple**: Begin with basic movements before complex behaviors
4. **Ask for help**: Share your code and describe what you're trying to do

Happy robot programming! 🚀
