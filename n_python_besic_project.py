========================================================================================================
1. Hello World project
========================================================================================================
def main():
    num = input("Enter a name: ")
    print(f"Hello, {num}!")


if __name__ == "__main__":
    main()
========================================================================================================
1. Calculator
========================================================================================================
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        try:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid input")
========================================================================================================
3. Even/Odd Checker
========================================================================================================
def modulus(num):
    return num % 2 == 0
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if modulus(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
========================================================================================================
4. Prime Number Checker
========================================================================================================
def prime():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    return num

if __name__ == "__main__":
    prime()
========================================================================================================
5. Factorial Calculator
========================================================================================================
6.Fibonacci Series
========================================================================================================
7.Multiplication Table
========================================================================================================
