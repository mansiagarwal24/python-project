# Q1. Define a function calculate_area that calculates the area of a rectangle and return the result. If no width is provided, it defaults to 10.

def calculate_area(l, b=10):
    return l*b

# Q2.  Write a recursive function to compute the factorial of a non-negative integer.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
#
# Q3. Write a function that takes one parameter as a string and reverse it and return.

def reverse(str):
    return str[::-1]
#
# Q4. Write a Python function that takes two parameters as lists and to sum all the numbers in a list.
# a = [8, 2, 3, 0, 7], b = [3, -2, 5, 1] and return a value.

def sum_lists(lst1, lst2):
    total =0
    for n in lst1:
        total += n
    for n in lst2:
        total += n
    return total
#
# Q5. Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list. a = [4,1,2,3,3,1,3,4,5,1,7]
# Output = [1,2,3,4,5,7]

def new_list_func(lst):
    distinct_lst = sorted(set(lst))
    return distinct_lst



def main():
    print(calculate_area(5))
    print(calculate_area(5,8))

    print("factorial",factorial(5))

    str = input("Enter a string: ")
    print(reverse(str))

    lst1 = [8, 2, 3, 0, 7]
    lst2 = [3, -2, 5, 1]
    print(sum_lists(lst1, lst2))

    lst = [4,1,2,3,3,1,3,4,5,1,7]
    print(new_list_func(lst))

main()
