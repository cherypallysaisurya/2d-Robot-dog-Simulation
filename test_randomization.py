#!/usr/bin/env python3
"""
Test the new randomized robot behaviors
"""

from robot_behavior import run_random_prime_bot, run_random_explorer

def test_randomization():
    print("🎲 Testing randomized robot behaviors...")
    
    # Test 1: Random prime bot (different starting position each time)
    print("\n1. Testing random prime bot...")
    run_random_prime_bot([2, 3, 4, 5, 6, 7])
    
    # Test 2: Random explorer
    print("\n2. Testing random explorer...")
    run_random_explorer(15)

if __name__ == "__main__":
    test_randomization()
