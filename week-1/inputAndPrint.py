# Q1. Objective: Ask the user for their name and greet them.
# Task: Write a program that asks the user for their name and then prints a greeting   message using their name.

def greetuser(name):
    print("good-morning " + name)

# Q2. Objective: Perform basic arithmetic operations based on user input.
# Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.

def arithmetic(num1,num2):
    sum = num1+num2
    print("sum", sum)
    product = num1 * num2
    print("product", product)
    division = num1/num2
    print("division" , division)


# Q3. Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.

def q3(names):
    list = names.split(",")
    print("list", list)

# Q4. Task: Ask the user to enter their age and check if they are eligible to vote based on their age.

def validate_age(age):
    if age >= 18 :
        print("You are eligible for vote.")
    else:
        print("you are not eligible for vote.")


# Q5. For value = 3.14159, Using f-string print output for only up to 2 decimal places.
# Output: 3.14

def func():
    value = 3.14159
    print(f"{value:.2f}")


def main():
    name = input("enter your name: ")
    greetuser(name)

    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    arithmetic(num1,num2)

    list = input("enter names: ")
    q3(list)

    age = int(input("enter your age: "))
    validate_age(age)

    func()


main()

