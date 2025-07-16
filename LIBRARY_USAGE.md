# Robot Behavior Library - Student Quick Start

## 🚀 Installation (One Time Setup)

```bash
# Download the library
git clone https://github.com/your-username/robot-behavior.git
cd robot-behavior

# Install globally (so you can use it anywhere)
pip install -e .
```

## 📚 Using the Library (Like Any Python Library)

### Simple Usage:
```python
# Import like any library (numpy, matplotlib, etc.)
from robot_behavior import *

# Use the pre-built robot functions
run_prime_bot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
run_spiral_bot(5)
run_square_bot(3)
```

### Custom Robot:
```python
from robot_behavior import *

# Create your own robot behavior
program = RobotProgram()

# Add obstacles
program.add_wall(3, 3)
program.add_wall(4, 4)

# Your custom logic
for i in range(10):
    if i % 3 == 0:
        program.robot.turn_left()
    else:
        program.robot.move_forward()

# Start simulation
program.start()
```

## 🎯 Available Functions

### Pre-built Robot Behaviors:
- `run_prime_bot(numbers)` - Robot moves for prime numbers
- `run_even_odd_bot(numbers)` - Robot turns based on even/odd
- `run_spiral_bot(steps)` - Robot moves in spiral pattern
- `run_square_bot(size)` - Robot moves in square pattern

### Building Blocks for Custom Robots:
- `RobotProgram()` - Create a new robot simulation
- `program.robot.move_forward()` - Move robot forward
- `program.robot.turn_left()` - Turn robot left
- `program.robot.turn_right()` - Turn robot right
- `program.add_wall(x, y)` - Add obstacle at position
- `is_prime(number)` - Check if number is prime

### Behavior Functions (for advanced users):
- `move_if_prime(robot, number)` - Move robot if number is prime
- `turn_if_even(robot, number)` - Turn robot based on even/odd
- `spiral_movement(robot, steps)` - Make robot move in spiral
- `square_movement(robot, size)` - Make robot move in square

## 📝 Student Template

Create a new file (e.g., `my_robot.py`) and use this template:

```python
from robot_behavior import *

def my_robot():
    # Create robot
    program = RobotProgram(width=12, height=12)
    
    # Add walls
    program.add_wall(5, 5)
    program.add_wall(6, 6)
    
    # Your logic here - modify this!
    my_numbers = [10, 15, 20, 25, 30]
    
    for num in my_numbers:
        if num % 5 == 0:  # Change this condition!
            program.robot.move_forward()
        else:
            program.robot.turn_right()
    
    # Start simulation
    program.simulator.root.after(3000, lambda: program.simulator.close())
    program.start()

# Run your robot
my_robot()
```

## 🎓 Learning Path

### Beginner:
1. Use `run_prime_bot([1,2,3,4,5])` with different numbers
2. Try `run_spiral_bot(3)` with different step counts
3. Modify the template above

### Intermediate:
1. Create custom logic with `RobotProgram()`
2. Add different wall patterns
3. Combine multiple behaviors

### Advanced:
1. Create new behavior functions
2. Use `move_if_prime()` and `turn_if_even()` directly
3. Build complex robot algorithms

## 💡 Project Ideas

- **Math Robot**: Robot that responds to different math sequences
- **Maze Solver**: Robot that navigates through obstacles
- **Pattern Drawer**: Robot that draws shapes and letters
- **Game Robot**: Robot that plays simple games on the grid
- **Algorithm Visualizer**: Robot that demonstrates sorting or search algorithms

Happy robot programming! 🤖
