# Write your code here


def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("The result is:", result)

def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("The result is:", result)

def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("The result is:", result)

def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print("The result is:", result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def detect_prime():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 1
    return factors

def generate_prime_factors():
    num = int(input("Enter a number: "))
    factors = prime_factors(num)
    if len(factors) == 1:
        print("The prime factorization of", num, "is", factors[0])
    else:
        print("The prime factorization of", num, "is", end=" ")
        for factor in factors[:-1]:
            print(factor, "*", end=" ")
        print(factors[-1])

def simplify_square_root():
    num = int(input("Enter a number: "))
    i = 2
    while i*i <= num:
        if num % (i*i) == 0:
            num //= (i*i)
        else:
            i += 1
    print("The simplified square root is", num)

def solve_equation():
    equation = input("Enter an equation to solve: ")
    # Add your code to solve the equation here
    print("The solution for the equation is:")

# Define the main function
def calculator():
    print("Welcome to the calculator!")
    print("Please select an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Detect prime numbers")
    print("6. Generate prime factors of a number")
    print("7. Simplify square roots")
    print("8. Solve for a variable")

    # Prompt the user to enter a choice
    choice = int(input("Enter your choice: "))

    # Execute different actions based on user input
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        detect_prime()
    elif choice == 6:
        generate_prime_factors()
    elif choice == 7:
        simplify_square_root()
    elif choice == 8:
        solve_equation()
    else:
     print("Invalid choice! Please choose again.")

calculator()


# This step does not have test
