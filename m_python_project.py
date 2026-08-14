========================================================================================================
1. Hello World project
========================================================================================================
def print_hello():
    name = input("Enter Your Name : ")
    print(f"Hello {name}")

if __name__ == "__main__":
    print_hello()
========================================================================================================
1. Calculator
========================================================================================================
option = input("please enter add, sub, mul div: ")
user1 = int(input("enter the first number:"))
user2 = int(input("enter the first number:"))

if option == "add":
    print(f"The sum of {user1} and {user2} is -{user1 + user2}")
elif option == "sub":
    print(f"The difference between {user1} and {user2} is -{user1 + user2}")
elif option == "mul":
    print(f"The product of {user1} and {user2} is -{user1 + user2}")
elif option == "div":
    print(f"The quotient of {user1} and {user2} is -{user1 + user2}")
else:
    print("invalid option. Please enter add, sub, mul, or div.")
========================================================================================================
3. Even/Odd Checker
========================================================================================================
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
========================================================================================================
4. Prime Number Checker
========================================================================================================
num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")
========================================================================================================
# Factorial Calculator
========================================================================================================

========================================================================================================
========================================================================================================
Fibonacci Series
Multiplication Table
Number Guessing Game
Rock Paper Scissors
Dice Rolling Simulator
Password Generator
BMI Calculator
Age Calculator
Unit Converter
Temperature Converter
Countdown Timer
Digital Clock
Alarm Clock
Calendar Program
Quiz Game
Hangman Game
To-Do List (CLI)
Contact Book
Student Grade System
========================================================================================================



