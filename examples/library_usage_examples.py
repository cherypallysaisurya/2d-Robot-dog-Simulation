# Student Examples - How to Use Robot Behavior Library
# Students can create files like this and import robot_behavior as a library

# ==============================================================================
#                           EXAMPLE 1: SIMPLE USAGE
# ==============================================================================

# Import the library (like importing numpy or matplotlib)
from robot_behavior import *

# Example 1: Test prime numbers
print("🔢 Testing prime number robot...")
run_prime_bot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19])

# Example 2: Test even/odd behavior  
print("🔄 Testing even/odd robot...")
run_even_odd_bot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Example 3: Draw patterns
print("🌀 Testing spiral robot...")
run_spiral_bot(5)

print("⬛ Testing square robot...")
run_square_bot(4)

# ==============================================================================
#                           EXAMPLE 2: CUSTOM ROBOT
# ==============================================================================

def my_custom_robot():
    """Example of creating your own robot behavior"""
    
    # Create a robot program
    program = RobotProgram(width=15, height=15)
    
    # Add obstacles
    program.add_wall(5, 5)
    program.add_wall(6, 6)
    program.add_wall(7, 7)
    
    # Your custom logic here!
    my_numbers = [10, 15, 20, 25, 30, 35]
    
    for num in my_numbers:
        if num % 5 == 0:  # Divisible by 5
            print(f"{num} is divisible by 5 - robot moves!")
            program.robot.move_forward()
        else:
            print(f"{num} is not divisible by 5 - robot turns!")
            program.robot.turn_right()
    
    # Close after 3 seconds
    program.simulator.root.after(3000, lambda: program.simulator.close())
    program.start()

# Run your custom robot
print("🎯 Testing custom robot...")
my_custom_robot()

# ==============================================================================
#                           EXAMPLE 3: USING BEHAVIOR FUNCTIONS
# ==============================================================================

def fibonacci_robot():
    """Create a robot that follows Fibonacci sequence"""
    
    program = RobotProgram(width=20, height=20)
    
    # Generate Fibonacci numbers
    fib_sequence = [1, 1]
    for i in range(8):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Use the behavior functions directly
    for num in fib_sequence[:10]:
        if is_prime(num):  # Use the is_prime function from the library
            move_if_prime(program.robot, num)
        else:
            turn_if_even(program.robot, num)
    
    program.simulator.root.after(4000, lambda: program.simulator.close())
    program.start()

print("🔢 Testing Fibonacci robot...")
fibonacci_robot()

# ==============================================================================
#                           EXAMPLE 4: SIMPLE STUDENT TEMPLATE
# ==============================================================================

def student_template():
    """Template for students to modify"""
    
    # Step 1: Create robot
    program = RobotProgram()
    
    # Step 2: Add walls (change these!)
    program.add_wall(3, 3)
    program.add_wall(4, 4)
    
    # Step 3: Your logic here (modify this!)
    for i in range(10):
        if i % 2 == 0:  # Even numbers
            program.robot.move_forward()
        else:  # Odd numbers
            program.robot.turn_left()
    
    # Step 4: Start simulation
    program.simulator.root.after(3000, lambda: program.simulator.close())
    program.start()

print("📝 Testing student template...")
student_template()

print("\n✅ All examples completed!")
print("📚 Now create your own file and use: from robot_behavior import *")
