# My Robot Experiments
# Student template - modify this file to create your own robots!

from robot_behavior import *

# ==============================================================================
#                    MODIFY THESE FUNCTIONS TO CREATE YOUR ROBOTS
# ==============================================================================

def my_first_robot():
    """Change this function to test different numbers"""
    
    # Try different numbers here!
    my_numbers = [2, 4, 6, 8, 10, 12, 14, 16]  # Even numbers
    
    print("🤖 My First Robot - Testing even numbers...")
    run_prime_bot(my_numbers)

def my_pattern_robot():
    """Change this function to create different patterns"""
    
    # Try different step counts!
    steps = 4  # Change this number
    
    print("🌀 My Pattern Robot - Creating spiral...")
    run_spiral_bot(steps)

def my_custom_robot():
    """Create your own robot logic here"""
    
    program = RobotProgram(width=15, height=15)
    
    # Add walls - change these positions!
    program.add_wall(3, 3)
    program.add_wall(7, 7)
    program.add_wall(10, 2)
    
    # Your custom logic - modify this!
    my_favorite_numbers = [5, 10, 15, 20, 25]
    
    for num in my_favorite_numbers:
        if num % 5 == 0:  # Divisible by 5 - change this condition!
            print(f"{num} is divisible by 5 - moving forward!")
            program.robot.move_forward()
        else:
            print(f"{num} is not divisible by 5 - turning!")
            program.robot.turn_right()
    
    # Auto-close after 4 seconds
    program.simulator.root.after(4000, lambda: program.simulator.close())
    program.start()

# ==============================================================================
#                              RUN YOUR ROBOTS
# ==============================================================================

if __name__ == "__main__":
    print("🚀 Welcome to Robot Programming!")
    print("Choose which robot to run:")
    print("1. My First Robot (prime numbers)")
    print("2. My Pattern Robot (spiral)")
    print("3. My Custom Robot (your logic)")
    
    choice = input("Enter choice (1-3) or press Enter for all: ").strip()
    
    if choice == "1":
        my_first_robot()
    elif choice == "2":
        my_pattern_robot()
    elif choice == "3":
        my_custom_robot()
    else:
        print("Running all robots...")
        my_first_robot()
        my_pattern_robot()
        my_custom_robot()

# ==============================================================================
#                              EXPERIMENT IDEAS
# ==============================================================================

"""
🎯 TRY THESE MODIFICATIONS:

1. Change Numbers:
   - Try prime numbers: [2, 3, 5, 7, 11, 13, 17, 19]
   - Try Fibonacci: [1, 1, 2, 3, 5, 8, 13, 21]
   - Try your birthday: [1, 2, 0, 5, 2, 0, 0, 3]

2. Change Conditions:
   - if num % 2 == 0:     # Even numbers
   - if num % 3 == 0:     # Divisible by 3
   - if num > 10:         # Numbers greater than 10
   - if num == 7:         # Only the number 7

3. Change Actions:
   - program.robot.move_forward()  # Move
   - program.robot.turn_left()     # Turn left
   - program.robot.turn_right()    # Turn right

4. Change Patterns:
   - run_spiral_bot(6)    # Bigger spiral
   - run_square_bot(5)    # Bigger square
   - run_even_odd_bot([1,2,3,4,5,6,7,8,9,10])  # More numbers

5. Add More Walls:
   program.add_wall(1, 1)
   program.add_wall(2, 2)
   program.add_wall(3, 3)
   # Create a maze!

💡 PROJECT IDEAS:
- Birthday Robot: Use digits from your birthday
- Name Robot: Convert letters to numbers (A=1, B=2, etc.)
- Math Robot: Test multiplication tables
- Maze Robot: Navigate through a complex maze
- Art Robot: Draw your initials on the grid
"""
