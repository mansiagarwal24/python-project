# Q1 Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
# Input : numbers = [1, 2, 3, 4, 5]
# #Expected Output : True

def check_positive_number():
    numbers = [1, 2, 3, 4, 5]
    res = all(num > 0 for num in numbers)
    print(res)

check_positive_number()

# Q2 Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
# Input: numbers = [1, 3, 5, 7, 8]
# #Expected Output: True

def check_even():
    numbers = [1, 3, 5, 7, 8]
    res = any(num % 2 == 0 for num in numbers)
    print(res)

check_even()

# Q3 Determine if any number in a list is divisible by 5 an print.

def check_divisible_by_5():
    number = [1,2,4,5,10,15]
    res = any(num for num in number if num % 5 ==0)
    print(res)

check_divisible_by_5()



