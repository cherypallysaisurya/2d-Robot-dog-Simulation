"""
Enhanced student example with randomization options.
Run this file to see both random and predictable robot behaviors!
"""

from robot_behavior.behaviors.api import (
    run_prime_bot,
    run_even_odd_bot,
    run_spiral_bot,
    run_square_bot,
    run_center_prime_bot,
    run_center_even_odd_bot,
    run_random_explorer,
    RobotProgram
)

def main():
    """Run all robot behavior examples with randomization options."""
    print("🤖 Robot Behavior Framework - Enhanced Examples")
    print("=" * 60)
    print("🎯 Features: Random starts, traces, walls, and variety!")
    print("=" * 60)
    
    # Example 1: Random starting robot
    print("\n1. Running RANDOM prime number robot...")
    print("   🎲 Robot starts at random position & direction")
    run_prime_bot([2, 3, 4, 5, 6, 7])  # Now random by default

    # Example 2: Predictable center-start robot  
    print("\n2. Running CENTER prime number robot...")
    print("   🎯 Robot starts at center for comparison")
    run_center_prime_bot([2, 3, 4, 5, 6, 7])

    # Example 3: Random even/odd robot
    print("\n3. Running RANDOM even/odd robot...")
    print("   🎲 Robot turns and moves from random position")
    run_even_odd_bot([1, 2, 3, 4, 5, 6])

    # Example 4: Random explorer
    print("\n4. Running RANDOM explorer...")
    print("   🗺️ Robot explores completely randomly")
    run_random_explorer(12)

    # Example 5: Custom robot with random start
    print("\n5. Running custom robot with RANDOM start...")
    print("   🔧 Custom behavior with randomization")
    custom_random_robot()

def custom_random_robot():
    """Example of a custom robot with random starting position."""
    # Create robot with random start
    program = RobotProgram(12, 12, random_robot=True)
    
    # Add some interesting walls
    program.add_wall(5, 5)
    program.add_wall(6, 6)
    program.add_wall(7, 5)
    
    print(f"🤖 Custom robot spawned at: {program.robot.get_position()}")
    print(f"🧭 Facing: {program.robot.get_direction().name}")
    
    # Custom behavior: Fibonacci sequence movement
    fibonacci = [1, 1, 2, 3, 5, 8]
    for fib in fibonacci:
        if fib % 2 == 0:  # Even Fibonacci numbers
            program.robot.turn_right()
            print(f"   {fib} is even → turned right")
        else:  # Odd Fibonacci numbers  
            moved = program.robot.move_forward()
            if moved:
                print(f"   {fib} is odd → moved forward")
            else:
                print(f"   {fib} is odd → couldn't move, hit obstacle")
    
    print("✅ Custom robot completed Fibonacci sequence!")
    program.simulator.root.after(4000, lambda: program.simulator.close())
    program.start()

    # Example 3: Spiral pattern - fixed grid size
    print("\n3. Running spiral pattern...")
    print("   Robot creates an outward spiral pattern")
    run_spiral_bot(4)  # Reduced layers for 10x10 grid

    # Example 4: Square pattern - consistent size
    print("\n4. Running square pattern...")
    print("   Robot moves in a square shape")
    run_square_bot(3)  # Reduced size for 10x10 grid

    # Example 5: Custom behavior with visible walls and traces
    print("\n5. Running custom behavior...")
    print("   Custom movement pattern with manual wall placement")
    
    # Create 10x10 program (consistent with others)
    program = RobotProgram(width=10, height=10)

    # Add walls that will be clearly visible
    walls_to_add = [
        (2, 2), (2, 3), (3, 2),  # Bottom left cluster
        (6, 6), (6, 7), (7, 6),  # Top right cluster  
        (8, 3), (8, 4), (9, 3),  # Right side cluster
        (1, 7), (1, 8)           # Top left
    ]
    
    print(f"   Adding {len(walls_to_add)} walls...")
    for wall_x, wall_y in walls_to_add:
        program.add_wall(wall_x, wall_y)

    print("   Starting custom movement pattern...")
    print("   Robot will move and turn, creating a visible trace")
    
    # Custom sequence that shows trace clearly
    for i in range(12):  # More moves to show better trace
        moved = program.robot.move_forward()
        print(f"   Move {i+1}: {'✓ Success' if moved else '✗ Blocked'}")
        
        if i % 3 == 0:
            program.robot.turn_right()
            print(f"     → Turned right")
        elif i % 3 == 1:
            program.robot.turn_left()
            print(f"     → Turned left")
        # Every 3rd move: no turn, just continue straight

    # Additional moves to show more trace
    print("   Additional forward moves...")
    for i in range(6):
        moved = program.robot.move_forward()
        print(f"   Extra move {i+1}: {'✓ Success' if moved else '✗ Blocked'}")

    print("   Auto-closing window in 8 seconds...")
    # Auto-close after 8 seconds to see the full trace
    program.simulator.root.after(8000, lambda: program.simulator.close())
    program.start()


if __name__ == "__main__":
    main()
