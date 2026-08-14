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
