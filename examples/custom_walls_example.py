#!/usr/bin/env python3
"""
Example showing how students can choose their own wall patterns
"""

from robot_behavior import run_prime_bot, run_even_odd_bot, run_random_explorer, RobotProgram

def demo_custom_walls():
    print("🏗️ Custom Wall Pattern Examples")
    print("=" * 50)
    
    # Example 1: Simple L-shaped wall pattern
    print("\n1. Prime bot with L-shaped walls:")
    l_shaped_walls = [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
    run_prime_bot([2, 3, 4, 5, 7], walls=l_shaped_walls)
    
    # Example 2: Cross pattern walls
    print("\n2. Even/Odd bot with cross pattern:")
    cross_walls = [(5, 3), (5, 7), (3, 5), (7, 5)]  # Cross in center
    run_even_odd_bot([1, 2, 3, 4, 5, 6], walls=cross_walls)
    
    # Example 3: Maze-like walls
    print("\n3. Explorer with maze-like walls:")
    maze_walls = [(1, 1), (1, 2), (3, 1), (3, 3), (5, 2), (5, 4), (7, 3), (7, 5)]
    run_random_explorer(15, walls=maze_walls)

def student_choice_walls():
    """Example where student can easily modify wall patterns"""
    print("\n🎯 Student Custom Wall Example")
    
    # Let students easily modify this list:
    my_walls = [
        (2, 2), (3, 2),     # Bottom wall
        (7, 7), (8, 7),     # Top wall  
        (1, 5), (2, 5),     # Left wall
        (8, 3), (9, 3)      # Right wall
    ]
    
    print(f"🧱 Using custom walls: {my_walls}")
    
    # Students can change the numbers and wall positions
    my_numbers = [2, 3, 5, 7, 11, 13]
    
    run_prime_bot(my_numbers, random_start=True, walls=my_walls)

def build_your_own():
    """Complete example of building custom robot with manual wall placement"""
    print("\n🔧 Build Your Own Robot with Custom Walls")
    
    # Create robot program
    program = RobotProgram(12, 12, random_robot=True)
    
    # Student can modify these wall coordinates
    student_walls = [
        (3, 3), (4, 3), (5, 3),  # Horizontal line
        (7, 5), (7, 6), (7, 7),  # Vertical line
        (9, 9), (10, 9),         # Corner obstacle
        (1, 8), (2, 8)           # Another obstacle
    ]
    
    print(f"🏗️ Adding walls at: {student_walls}")
    for x, y in student_walls:
        program.add_wall(x, y)
    
    # Custom movement logic
    print(f"🤖 Robot starts at: {program.robot.get_position()}")
    
    # Student can modify this behavior
    for i in range(10):
        if i % 2 == 0:
            program.robot.move_forward()
        else:
            program.robot.turn_right()
    
    # Keep window open to see result
    program.simulator.root.after(5000, lambda: program.simulator.close())
    program.start()

if __name__ == "__main__":
    print("Choose an example:")
    print("1. Demo custom wall patterns")
    print("2. Student choice walls")
    print("3. Build your own robot")
    
    choice = input("Enter 1, 2, or 3: ").strip()
    
    if choice == "1":
        demo_custom_walls()
    elif choice == "2":
        student_choice_walls()
    elif choice == "3":
        build_your_own()
    else:
        print("Invalid choice, running student choice example...")
        student_choice_walls()
