# 🤖 Robot Behavior Simulator

An educational Python package that teaches programming concepts through a visual robot simulation. Perfect for beginners learning their first programming concepts!

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Education](https://img.shields.io/badge/purpose-education-orange)

## 🎯 What This Package Does

The Robot Behavior Simulator creates an interactive visual environment where students control a robot (displayed as a blue triangle arrow) moving around a grid. As the robot moves, it draws a **red trail** showing its path, making programming concepts immediately visible and engaging.

### 🌟 Key Features

- **🤖 Visual Robot**: Blue triangle arrow that points east and moves smoothly
- **🔴 Red Trail Visualization**: See exactly where your robot has been
- **🧱 Obstacles & Walls**: Navigate around barriers and solve maze challenges  
- **⚡ Immediate Feedback**: Instant visual results help students understand their code
- **📚 Educational Focus**: Designed specifically for teaching programming fundamentals

## 🚀 Quick Installation

Install the package using pip:

```bash
pip install robot-behavior-simulator
```

## 🎮 Basic Usage

### Simple Movement Example

```python
from robot_behavior import create_robot_program

# Create a 5x5 grid with robot starting at position (0, 0)
program = create_robot_program(5, 5, 0, 0)

# Add some walls to make it interesting
program.add_wall(2, 0)
program.add_wall(3, 1)

# Move the robot and watch the red trail appear!
program.robot.move('right')  # Move east
program.robot.move('right')  # Move east again  
program.robot.move('up')     # Move north
program.robot.move('backward')  # Move west (opposite of facing direction)

# Start the visual display
program.start_with_auto_close(5)  # Close after 5 seconds
```

### Fun Pattern Example

```python
from robot_behavior import create_robot_program

# Create robot world
program = create_robot_program(8, 8, 1, 1)

# Draw a square pattern
movements = ['right', 'right', 'up', 'up', 'left', 'left', 'down', 'down']
for direction in movements:
    success = program.robot.move(direction)
    if not success:
        print(f"Can't move {direction} - hit a wall!")

program.start_with_auto_close(10)
```

## 🎓 Educational Concepts Taught

This simulator helps students learn:

### 1. **Sequential Programming**
```python
robot.move('right')  # Step 1
robot.move('up')     # Step 2  
robot.move('left')   # Step 3
# Each command executes in order
```

### 2. **Conditional Logic**
```python
success = robot.move('right')
if success:
    print("Robot moved successfully!")
else:
    print("Hit a wall - need to try different direction")
```

### 3. **Loops and Patterns**
```python
# Draw a square
for side in range(4):
    for step in range(3):
        robot.move('right')
    # Change direction for next side
```

### 4. **Problem Solving**
Students learn to navigate mazes, avoid obstacles, and plan efficient paths.

## 📚 Complete API Reference

### Core Functions
- `create_robot_program(width, height, start_x, start_y)` - Create robot world
- `robot.move(direction)` - Move robot ('up', 'down', 'left', 'right', 'backward')
- `robot.get_position()` - Get current position
- `program.add_wall(x, y)` - Add wall/obstacle
- `program.start()` - Start visual simulator

### Available Directions
- `'up'` - Move north (y + 1)
- `'down'` - Move south (y - 1)  
- `'left'` - Move west (x - 1)
- `'right'` - Move east (x + 1)
- `'backward'` - Move opposite to facing direction (west, since dog faces east)

## 🎯 Perfect for Learning

### For Students:
- **Visual feedback** makes abstract concepts concrete
- **Immediate results** keep engagement high
- **Error handling** teaches debugging skills
- **Creative freedom** allows artistic expression through code

### For Educators:
- **Minimal setup** - just `pip install` and go
- **Progressive complexity** - start simple, add challenges
- **Clear visual results** for easy assessment
- **Engaging format** keeps students motivated

## 🔧 Requirements

- Python 3.7 or higher
- Pillow (for image handling) - automatically installed

## 📖 More Examples

Check out the `examples/` directory for more educational examples:
- Basic movement patterns
- Maze solving algorithms
- Creative drawing with code
- Problem-solving challenges

## 🤝 Contributing

This project is designed for educational use. Contributions that enhance the learning experience are welcome!

## 📄 License

MIT License - feel free to use in educational settings.

## 👨‍💻 Authors

Robot Behavior Simulator Team - Dedicated to making programming education visual and engaging.

---

**Happy Coding! 🚀** Let's make programming education visual, interactive, and fun!
