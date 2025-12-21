# Q1 Write a Python program that attempts to divide two numbers a = 10  b = 0
# and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error

def division(a,b):
    try:
        print (a/b)
    except ZeroDivisionError as err:
        print (err)

division(10,0)

# Q2 Apply exception handling to below code and handle an exception if the index is out of range.
# my_list = [1, 2, 3]
# print(my_list[5])

def handle_exception():
    try:
        my_list = [1, 2, 3]
        n= my_list[5]
        print(n)
    except IndexError as err:
        print("index out of range")

handle_exception()

# Q3 Correct this below code with appropriate exception handlings. And finally print “Execution completed”
def safe_divide(a,b):
    try:
      result = a / b
      print(f"Result: {result}")
    except ZeroDivisionError:
      print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both values must be numbers.")
    finally:
        print("Execution completed")

safe_divide(1, 0)
safe_divide(1, "a")


# def main():
#     print(division(10,0))
#     handle_exception()
#
#
# main()
