# Student Template - Copy this to create your own robot!
# Save as: my_robot_[your_name].py

from robot_behavior.behaviors.api import RobotProgram, run_prime_bot
from robot_behavior.behaviors.basic import move_if_prime, turn_if_even

# ==============================================================================
#                           YOUR ROBOT PLAYGROUND
# ==============================================================================

def my_number_robot():
    """Example: Create a robot that responds to your favorite numbers"""
    
    # Your favorite numbers (change these!)
    favorite_numbers = [7, 14, 21, 28, 35]  # Multiples of 7
    
    program = RobotProgram(width=12, height=12)
    
    # Add some obstacles (change positions!)
    program.add_wall(3, 3)
    program.add_wall(5, 5)
    program.add_wall(7, 2)
    
    # Your custom logic here!
    for num in favorite_numbers:
        if num % 7 == 0:  # If divisible by 7
            print(f"{num} is divisible by 7 - robot moves!")
            program.robot.move_forward()
        else:
            print(f"{num} is not divisible by 7 - robot turns!")
            program.robot.turn_right()
    
    # Auto-close after 3 seconds
    program.simulator.root.after(3000, lambda: program.simulator.close())
    program.start()

def my_pattern_robot():
    """Example: Create a robot that draws your initials or a pattern"""
    
    program = RobotProgram(width=15, height=15)
    
    # Add walls to create boundaries
    program.add_wall(8, 8)
    program.add_wall(9, 8)
    program.add_wall(10, 8)
    
    # Draw a simple "L" shape (change this to your initials!)
    # Vertical line
    for _ in range(5):
        program.robot.move_forward()
    
    # Turn and horizontal line
    program.robot.turn_right()
    for _ in range(3):
        program.robot.move_forward()
    
    # Auto-close after 4 seconds
    program.simulator.root.after(4000, lambda: program.simulator.close())
    program.start()

def my_maze_solver():
    """Example: Create a robot that navigates through a maze"""
    
    program = RobotProgram(width=15, height=15)
    
    # Create a simple maze (change the layout!)
    maze_walls = [
        (2, 1), (2, 2), (2, 3), (2, 4),
        (4, 1), (4, 2), (4, 3), (4, 4),
        (6, 2), (6, 3), (6, 4), (6, 5),
        (8, 1), (8, 2), (8, 3), (8, 4)
    ]
    
    for wall_x, wall_y in maze_walls:
        program.add_wall(wall_x, wall_y)
    
    # Simple maze navigation: go forward, if blocked turn right
    for _ in range(20):  # Try 20 moves
        moved = program.robot.move_forward()
        if not moved:  # If we hit a wall
            program.robot.turn_right()
            print("Hit wall - turning right!")
    
    # Auto-close after 5 seconds
    program.simulator.root.after(5000, lambda: program.simulator.close())
    program.start()

def my_fibonacci_robot():
    """Advanced: Robot that moves in Fibonacci sequence pattern"""
    
    program = RobotProgram(width=20, height=20)
    
    # Fibonacci sequence
    a, b = 1, 1
    
    for i in range(8):  # First 8 Fibonacci numbers
        print(f"Fibonacci step {i+1}: moving {a} spaces")
        
        # Move 'a' number of spaces
        for _ in range(min(a, 10)):  # Cap at 10 to stay on grid
            program.robot.move_forward()
        
        # Turn for next direction
        program.robot.turn_right()
        
        # Next Fibonacci number
        a, b = b, a + b
    
    # Auto-close after 6 seconds
    program.simulator.root.after(6000, lambda: program.simulator.close())
    program.start()

# ==============================================================================
#                              RUN YOUR ROBOTS
# ==============================================================================

if __name__ == "__main__":
    print("🤖 Welcome to your robot playground!")
    print("Choose which robot to run:")
    print("1. Number Robot")
    print("2. Pattern Robot (draws 'L')")
    print("3. Maze Solver")
    print("4. Fibonacci Robot")
    print("5. Run all examples")
    
    choice = input("Enter choice (1-5): ").strip()
    
    if choice == "1":
        print("Running Number Robot...")
        my_number_robot()
    elif choice == "2":
        print("Running Pattern Robot...")
        my_pattern_robot()
    elif choice == "3":
        print("Running Maze Solver...")
        my_maze_solver()
    elif choice == "4":
        print("Running Fibonacci Robot...")
        my_fibonacci_robot()
    elif choice == "5":
        print("Running all examples...")
        my_number_robot()
        my_pattern_robot()
        my_maze_solver()
        my_fibonacci_robot()
    else:
        print("Invalid choice. Running Number Robot as default...")
        my_number_robot()

# ==============================================================================
#                               CUSTOMIZATION TIPS
# ==============================================================================

"""
🎯 EASY CUSTOMIZATIONS:

1. Change Numbers:
   - Modify favorite_numbers list
   - Try different mathematical conditions (even/odd, divisible by X)

2. Change Patterns:
   - Draw your initials instead of "L"
   - Create geometric shapes (triangle, diamond)

3. Change Maze:
   - Modify maze_walls list to create new layouts
   - Add more walls or remove some

4. Change Behavior:
   - Add more turns, different movement patterns
   - Combine multiple conditions

🔧 INTERMEDIATE CUSTOMIZATIONS:

1. Add New Logic:
   def is_perfect_square(n):
       return int(n ** 0.5) ** 2 == n
   
   if is_perfect_square(num):
       robot.move_forward()

2. Add Color/Visual Changes:
   - Modify simulator.py to change colors
   - Add different robot shapes

3. Add Sound:
   - Use winsound (Windows) or pygame for sound effects

💡 IDEAS FOR NEW ROBOTS:

- Birthday Robot: Moves based on dates
- ASCII Art Robot: Draws letters/pictures
- Calculator Robot: Performs math visually
- Game Robot: Plays tic-tac-toe on the grid
- Sensor Robot: Responds to "virtual sensors"
"""
