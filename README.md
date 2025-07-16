# 🤖 Robot Behavior Framework

A simple, educational 2D robot simulation library for learning programming concepts through visual robot behaviors.

**Use it like any Python library:**
```python
from robot_behavior import *
run_prime_bot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
```

## ✨ Features

- 🎮 **Easy to use** - Import like numpy or matplotlib
- 🎯 **Educational** - Focus on logic, not complex setup  
- 🎨 **Visual** - See your code come to life with moving robots
- 🚧 **Obstacle-aware** - Robots avoid walls and boundaries
- 📝 **Well-documented** - Clear examples and templates
- 🌐 **Cross-platform** - Works on Windows, Mac, Linux
- 🔧 **Extensible** - Easy to add new behaviors

## 🚀 Quick Start

### Installation
```bash
pip install git+https://github.com/your-username/robot-behavior.git
```

### Use It
```python
from robot_behavior import *

# Pre-built behaviors
run_prime_bot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
run_spiral_bot(5)
run_square_bot(3)

# Custom robot
program = RobotProgram()
program.add_wall(3, 3)
for i in range(10):
    if i % 2 == 0:
        program.robot.move_forward()
    else:
        program.robot.turn_right()
program.start()
```

## 📚 Available Functions

### 🎯 Pre-built Robot Behaviors
| Function | Description | Example |
|----------|-------------|---------|
| `run_prime_bot(numbers)` | Robot moves for prime numbers | `run_prime_bot([2,3,4,5,6,7])` |
| `run_even_odd_bot(numbers)` | Robot turns based on even/odd | `run_even_odd_bot([1,2,3,4,5])` |
| `run_spiral_bot(steps)` | Robot moves in spiral pattern | `run_spiral_bot(5)` |
| `run_square_bot(size)` | Robot moves in square pattern | `run_square_bot(4)` |

### 🔧 Building Blocks for Custom Robots
| Function | Description |
|----------|-------------|
| `RobotProgram()` | Create a new robot simulation |
| `program.robot.move_forward()` | Move robot forward |
| `program.robot.turn_left()` | Turn robot left |
| `program.robot.turn_right()` | Turn robot right |
| `program.add_wall(x, y)` | Add obstacle at position |
| `is_prime(number)` | Check if number is prime |

## 🎓 Learning Examples

### Beginner: Use Pre-built Functions
```python
from robot_behavior import *

# Test different number sequences
run_prime_bot([2, 3, 5, 7, 11, 13, 17, 19])
run_even_odd_bot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

### Intermediate: Create Custom Logic
```python
from robot_behavior import *

program = RobotProgram(width=15, height=15)
program.add_wall(5, 5)
program.add_wall(6, 6)

# Custom logic: Move for multiples of 3
for num in [3, 6, 9, 12, 15, 18]:
    if num % 3 == 0:
        program.robot.move_forward()
    else:
        program.robot.turn_right()

program.start()
```

### Advanced: Build New Behaviors
```python
from robot_behavior import *

def fibonacci_robot():
    program = RobotProgram(width=20, height=20)
    
    # Generate Fibonacci sequence
    a, b = 1, 1
    for i in range(8):
        # Move 'a' steps
        for _ in range(min(a, 5)):
            program.robot.move_forward()
        program.robot.turn_right()
        a, b = b, a + b
    
    program.start()

fibonacci_robot()
```

## 💡 Project Ideas

- **📊 Math Visualizer**: Robot that demonstrates number sequences
- **🎮 Maze Solver**: Robot that navigates through obstacles  
- **🎨 Pattern Drawer**: Robot that draws shapes and letters
- **🧮 Algorithm Demo**: Robot that shows sorting or searching
- **🎯 Custom Logic**: Robot that responds to your own rules

## 📁 Example Files

- [`examples/library_usage_examples.py`](examples/library_usage_examples.py) - Complete usage examples
- [`examples/student_playground.py`](examples/student_playground.py) - Template for experimentation
- [`LIBRARY_USAGE.md`](LIBRARY_USAGE.md) - Detailed documentation

## 🎯 Educational Use

Perfect for:
- **Programming courses** - Visualize logic concepts
- **Algorithm classes** - Demonstrate pathfinding, patterns
- **Math classes** - Explore number sequences visually
- **Self-learning** - Fun way to practice Python

## 🛠️ Requirements

- Python 3.7+
- Tkinter (included with Python)
- numpy

No complex dependencies, game engines, or setup required!

## 📖 Documentation

- [Student Setup Guide](STUDENT_SETUP_GUIDE.md) - Complete installation instructions
- [Library Usage](LIBRARY_USAGE.md) - Detailed function documentation  
- [Distribution Guide](DISTRIBUTION_GUIDE.md) - How to share with others

## 🤝 Contributing

This is an educational project. Students are encouraged to:
1. Fork the repository
2. Add new robot behaviors
3. Share their creations
4. Help improve documentation

## 📄 License

MIT License - feel free to use for educational purposes!

---

**🎉 Start coding your robots today!**

```python
from robot_behavior import *
run_prime_bot([2, 3, 5, 7, 11, 13, 17, 19, 23])
```
