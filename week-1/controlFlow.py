# For loop
# 1. Write a program that takes the input from the user and checks if a number is even or odd.
import string

def odd_even(num):
    if num % 2  == 0:
        print("number is even")
    else :
        print("number is odd")

# 2. Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”

def reverse(str1):
    rev = ""
    for ch in str1:
        rev = ch + rev
    print("reversed string: ", rev)
    if rev == str1 :
        print("palindrome")
    else:
        print(" not a palindrome")

# 3. Using the input from the user, Generate the first N numbers of the Fibonacci sequence.

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

# 4. From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]

def func(lst, val):
    for i in range(len(lst)-1):
        num = lst[i] + lst[i+1]
        if num == val:
            return lst[i], lst[i + 1]
    return None

# While loop
# 5. Print all even numbers between 1 and 20 using a while loop.

def even():
    i=1
    while i<=20:
        if i % 2 == 0:
            print(i, end=" ")
        i=i+1

# Break
# 6. Find the first occurrence of a number in a list and stop further searching.
# numbers = [10, 20, 30, 40, 50]
# search_for = 30

def search():
    numbers = [10, 20, 30, 40, 50]
    val = 30
    for num in numbers:
        if num == val :
            print(num, end=" ")
            break

# Continue
# 7. Using continue statement, print only the odd numbers from 1 to 10.

def print_odd():
    for i in range(10):
        if i % 2 == 0 :
            continue
        print(i, end=" ")

# Pass
# 8. What will be the output
# for i in range(5):
#     if i == 3:
#         pass
#     print(i)

def fun_output():
    for i in range(5):
        if i == 3:
            pass
        print(i)

#output : 1,2,3,4


# Match
# 9. Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.

def check_day():
    day = input("Enter a day of the week: ").lower()

    match day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("It's a weekday.")
        case "saturday" | "sunday":
            print("It's a weekend.")
        case _:
            print("Invalid day entered.")


def main():
    num = int(input("Enter a number: "))
    odd_even(num)

    str1 = input("Enter a string: ")
    reverse(str1)

    lst = input("Enter a list: ")
    val = int(input("Enter a number: "))
    print(func(lst, val))

    fibo(8)
    search()
    print_odd()
    even()
    fun_output()
    check_day()


main()
