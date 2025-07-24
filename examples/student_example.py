"""
Enhanced student example with randomization options.
Run this file to see both random and predictable robot behaviors!
"""

from robot_behavior.behaviors.api import (
    run_prime_bot,
    run_even_odd_bot,
    run_spiral_bot,
    run_square_bot,
    run_random_explorer,
    RobotProgram
)

def main():
    """Run all robot behavior examples with basic functionality."""
    print("🤖 Robot Behavior Framework - Basic Examples")
    print("=" * 60)
    print("🎯 Features: Prime numbers, patterns, and exploration!")
    print("=" * 60)
    
    # Example 1: Prime number robot
    print("\n1. Running prime number robot...")
    print("   🔢 Robot moves only on prime numbers")
    run_prime_bot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    # Example 2: Even/odd robot  
    print("\n2. Running even/odd robot...")
    print("   🔄 Robot turns based on even/odd numbers")
    run_even_odd_bot([1, 2, 3, 4, 5, 6])

    # Example 3: Spiral pattern
    print("\n3. Running spiral pattern robot...")
    print("   � Robot creates a spiral pattern")
    run_spiral_bot(6)

    # Example 4: Square pattern
    print("\n4. Running square pattern robot...")
    print("   ⬜ Robot moves in a square shape")
    run_square_bot(3)

    # Example 5: Random explorer
    print("\n5. Running random explorer...")
    print("   🗺️ Robot explores randomly with obstacles")
    run_random_explorer(15)

    # Example 6: Custom robot behavior
    print("\n6. Running custom robot behavior...")
    print("   🔧 Custom programming example")
    custom_fibonacci_robot()

def custom_fibonacci_robot():
    """Example of a custom robot following Fibonacci sequence."""
    # Create robot program
    program = RobotProgram(12, 12)
    
    # Add some interesting walls
    program.add_wall(5, 5)
    program.add_wall(6, 6)
    program.add_wall(7, 5)
    program.add_wall(3, 7)
    
    print(f"🤖 Custom Fibonacci robot starting at: {program.robot.get_position()}")
    print(f"🧭 Facing: {program.robot.get_direction().name}")
    
    # Custom behavior: Fibonacci sequence movement
    fibonacci = [1, 1, 2, 3, 5, 8, 13]
    for i, fib in enumerate(fibonacci):
        if fib % 2 == 0:  # Even Fibonacci numbers
            program.robot.turn_right()
            print(f"   Step {i+1}: {fib} is even → turned right")
        else:  # Odd Fibonacci numbers  
            moved = program.robot.move_forward()
            if moved:
                print(f"   Step {i+1}: {fib} is odd → moved forward")
            else:
                print(f"   Step {i+1}: {fib} is odd → couldn't move, hit obstacle")
    
    print("✅ Custom Fibonacci robot completed sequence!")
    program.simulator.root.after(4000, lambda: program.simulator.close())
    program.start()


if __name__ == "__main__":
    main()
