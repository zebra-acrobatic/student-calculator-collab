#!/usr/bin/env python3
"""
Simple Calculator - Student Collaboration Project
Basic calculator with room for student enhancements
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract second number from first and return the result."""
    return a - b

def get_number(prompt):
    """Get a valid number from user input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def get_operation():
    """Get a valid operation from user input."""
    valid_operations = ['+', '-']
    while True:
        operation = input(f"Choose operation ({', '.join(valid_operations)}): ").strip()
        if operation in valid_operations:
            return operation
        print(f"❌ Please choose from: {', '.join(valid_operations)}")

def start():
    """Main calculator function."""
    print("=" * 30)
    print("🧮 STUDENT CALCULATOR v1.0")
    print("=" * 30)
    print("Welcome! This calculator supports basic operations.")
    print("More features coming soon through student contributions!\n")
    
    while True:
        try:
            # Get inputs
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            operation = get_operation()
            
            # Perform calculation
            if operation == '+':
                result = add(num1, num2)
                print(f"✅ {num1} + {num2} = {result}")
            elif operation == '-':
                result = subtract(num1, num2)
                print(f"✅ {num1} - {num2} = {result}")
            
            # Continue or exit
            print("\n" + "-" * 30)
            continue_calc = input("Calculate again? (y/n): ").strip().lower()
            if continue_calc not in ['y', 'yes']:
                break
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Thanks for using the calculator!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("Please try again.")
    
    print("Goodbye! 👋")

start()
