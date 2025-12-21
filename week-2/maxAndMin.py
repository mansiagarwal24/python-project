# Q1 Find the Maximum and Minimum Values in a List
# numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]

def max_min_list():
    numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
    print(max(numbers))
    print(min(numbers))

max_min_list()


# Q2 Given a set of numbers, find the maximum and minimum values.
# setn = {5, 10, 3, 15, 2, 20}

def max_min_number():
    setn = {5, 10, 3, 15, 2, 20}
    print(max(setn))
    print(min(setn))

max_min_number()


# Q3 Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order.
# If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
#
# Input: words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
# Output: ('kiwi', 'grapefruit')

def shortest_longest(words):
    shortest = longest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word
    return shortest, longest

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print(shortest_longest(words))
