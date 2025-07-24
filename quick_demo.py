"""
🎯 QUICK DEMO - Robot Behavior Framework
=======================================

A concise demonstration of the educational robot simulation package
Perfect for: Quick presentations, time-constrained demos, overview sessions

Run this for a fast 5-minute demo of key features!
"""

from robot_behavior.behaviors.api import (
    run_prime_bot,
    run_even_odd_bot,
    run_spiral_bot,
    run_random_explorer,
    RobotProgram
)
import time

def quick_demo():
    """5-minute comprehensive demo of the robot framework."""
    
    print("🎓 ROBOT BEHAVIOR FRAMEWORK - PROFESSOR DEMO")
    print("=" * 55)
    print("This Python package teaches programming through visual robot simulations!")
    print("Each demonstration will run automatically with a 2-second delay between demos.")
    print()
    
    # Demo 1: Prime Numbers (Mathematical Logic)
    print("1️⃣ MATHEMATICAL LOGIC - Prime Number Robot")
    print("   🔢 Robot moves only on prime numbers (2,3,5,7,11)...")
    time.sleep(2)
    run_prime_bot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    # Demo 2: Decision Making (Even/Odd Logic)  
    print("\n2️⃣ DECISION MAKING - Even/Odd Robot")
    print("   ⚡ Robot turns left on odd, right on even numbers...")
    time.sleep(2)
    run_even_odd_bot([1, 2, 3, 4, 5, 6, 7, 8])
    
    # Demo 3: Pattern Generation (Spiral Algorithm)
    print("\n3️⃣ ALGORITHMIC PATTERNS - Spiral Robot") 
    print("   🌀 Robot creates expanding spiral pattern...")
    time.sleep(2)
    run_spiral_bot(5)
    
    # Demo 4: Intelligent Navigation
    print("\n4️⃣ INTELLIGENT NAVIGATION - Explorer Robot")
    print("   🗺️ Robot navigates around random obstacles intelligently...")
    time.sleep(2)
    run_random_explorer(15)
    
    # Demo 5: Student Creativity Example
    print("\n5️⃣ STUDENT CREATIVITY - Temperature Control Robot")
    print("   🌡️ Student-created robot responds to temperature data...")
    time.sleep(2)
    
    # Quick custom robot example
    program = RobotProgram(12, 12)
    program.simulator.set_title_label("🌡️ Temperature Control Robot - Student Creation")
    program.add_wall(5, 7)
    program.add_wall(7, 5)
    
    temperatures = [18, 25, 32, 15, 28, 35, 12, 30]  # Temperature readings
    
    for temp in temperatures:
        if temp > 30:  # Hot temperature
            program.robot.turn_right()  # "Turn on AC"
        elif temp < 20:  # Cold temperature  
            program.robot.turn_left()   # "Turn on heater"
        else:  # Comfortable temperature
            program.robot.move_forward()  # "Move forward"
        time.sleep(0.4)
    
    program.simulator.root.after(3000, lambda: program.simulator.close())
    program.start()
    
    # Conclusion
    print("\n🎯 DEMO COMPLETE!")
    print("=" * 55)
    print("✅ Framework teaches programming through visual robotics")
    print("✅ Students learn: logic, math, algorithms, creativity") 
    print("✅ Ready for classroom use with documentation & examples")
    print()
    print("🔗 GitHub: https://github.com/cherypallysaisurya/2d-Robot-dog-Simulation")

if __name__ == "__main__":
    print("🚀 Starting Quick Demo of Robot Behavior Framework...")
    print()
    
    try:
        quick_demo()
    except KeyboardInterrupt:
        print("\n⏹️ Demo stopped by user. Thank you!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check installation: pip install git+[repository-url]")
