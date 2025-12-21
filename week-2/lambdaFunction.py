from functools import reduce

# Q1 Given a list let's see how to double each element of the given list. Using map()
# a = [1, 2, 3, 4]
# #Expected Output: [2, 4, 6, 8]

def map_func():
    a = [1, 2, 3, 4]
    res = list(map(lambda x : x * 2 , a))
    print(res)

#  Q2 Use filter() and lambda to extract all even numbers from a list of integers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #Expected Output: [2, 4, 6, 8, 10]

def even_func():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = list(filter(lambda x : x % 2 == 0 , numbers))
    print(res)

# Q3 Use reduce() and lambda to find the longest word in a list of strings.
# from functools import reduce
# words = ["apple", "banana", "cherry", "date"]
# #Expected Output: 'banana'

def reduce_func():
    words = ["apple", "banana", "cherry", "date"]
    res = reduce(lambda a, b: a if len(a) > len(b) else b, words)
    print(res)


# Q4 Use map() to square each number in the list and round the result to one decimal place.
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# #Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]

def round_func():
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
    res = list(map(lambda x : round(x ** 2, 1), my_floats))
    print(res)


# Q5 Use filter() to select names with 7 or fewer characters from the list.
# 	my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# 	#Expected Output: ['olumide', 'josiah', 'omoseun']

def filter_func():
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
    res = list(filter(lambda x : len(x)<= 7 , my_names))
    print(res)


# Q6 Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]

def sum_func():
    numbers = [1, 2, 3, 4, 5]
    sum = reduce(lambda x, y: x + y , numbers)
    print(sum)


def main():
    map_func()
    even_func()
    reduce_func()
    round_func()
    filter_func()
    sum_func()

main()