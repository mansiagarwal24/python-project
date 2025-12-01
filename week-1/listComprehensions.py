# Q1. Given a list of numeric strings, convert them into integers. Using List Comprehensions
# strings = ["1", "2", "3", "4", "5"]
# #Expected output : [1, 2, 3, 4, 5]

def list_of_strings():
    strings = ["1", "2", "3", "4", "5"]
    integers_lst = [int(x) for x in strings]
    return integers_lst

# Q2. Extract all integers from a list that are greater than 10. Using List Comprehensions
# numbers = [1, 5, 13, 4, 16, 7]
# #Expected output :[13, 16]

def new_list():
    numbers = [1, 5, 13, 4, 16, 7]
    lst = [x for x in numbers if x > 10]
    return lst

# Q3. Create a list of squares for numbers from 1 to 5. Using List Comprehensions
# #Expected output :[1, 4, 9, 16, 25]

def list_of_square():
    squares = [x**2 for x in range(1,6)]
    return squares

# Q4. Convert a 2D list into a 1D list.Using List Comprehensions
# matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
# #Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]

def matrix():
    matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
    matrix_list = [num for row in matrix for num in row]
    return matrix_list


# Q5. Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
# #Expected output : {'a': 1, 'b': 2, 'c': 3}

def new_dict():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    my_dict = dict(zip(keys, values))
    return my_dict


# Q6. Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
# 	#Expected output : {'Alice': 85, 'Charlie': 90}

def dict1():
    scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
    filtered_scores =  {name: score for name, score in scores.items() if score > 80}
    return filtered_scores


def main():
    print(list_of_strings())
    print(new_list())
    print(list_of_square())
    print(matrix())
    print(new_dict())
    print(dict1())


main()
