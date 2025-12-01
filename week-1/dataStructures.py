# Q1. Given a list of numbers, find and print the maximum and minimum values.
#               nums = [1, 2, 3, 4, 5]
def func1():
    list1 = [1,2,3,4,5,6,7,8,9]
    print("max num:",max(list1))
    print("min num:",min(list1))

# Q2. Given two lists below, merge the values from both lists to one and print
#              a = [1,2,3,4]      b = [5,6,7,8]

def func2():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    a.extend(b)
    print(a)

# Q3. From a list, print the number of times the value 3 appears in the list:
# 		a = [1,3,4,5,2,1,3,9,3]

def func3():
    a = [1,3,4,5,2,1,3,9,3]
    count = list.count(a,3)
    print(count)

# Q4. From below list, Sort the list and print
# 		a = [1,3,4,5,2,1,3,9,3]

def func4():
    a = [1,3,4,5,2,1,3,9,3]
    a.sort()
    print(a)

# Q5. Given a set, add the element 6 to it and print the updated set.
#                numbers = {1, 2, 3, 4, 5}

def func5():
    numbers = {1, 2, 3, 4, 5}
    numbers.add(6)
    print(numbers)

# Q6. Given a set, remove the element 3 from it and print the updated set.
# 		numbers = {1, 2, 3, 4, 5}

def func6():
    numbers = {1, 2, 3, 4, 5}
    numbers.remove(3)
    print(numbers)

# Q7. Given two sets, find and print their intersection.
# 		set1 = {1, 2, 3}    set2 = {3, 4, 5}

def func7():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    value = set.intersection(set1, set2)
    print(value)

# Q8. Given a tuple, count and print the number of occurrences of the element 'apple'.
# 		fruits = ('apple', 'banana', 'apple', 'cherry')

def func8():
    fruits = ('apple', 'banana', 'apple', 'cherry')
    print(fruits.count('apple'))

# Q9. Given two tuples, concatenate them and print the result.
# 		tuple1 = (1, 2, 3)     tuple2 = (4, 5, 6)

def func9():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    res  = tuple1 + tuple2
    print(res)

# Q10. Access and print the value associated with the key "age" from the dictionary.
# 		person = {"name": "Alice", "age": 30, "city": "New York"}

def func10():
    person = {"name": "Alice", "age": 30, "city": "New York"}
    age = person["age"]
    print(age)

# Q11. Add new key,  gender to dictionary and assign “M” to it and print
# person = {"name": "Alice", "age": 30, "city": "New York"}

def func11():
    person = {"name": "Alice", "age": 30, "city": "New York"}
    person["gender"] = "M"
    print(person)

# Q12. Remove the key "city" from the above Dict and print

def func12():
    person = {"name": "Alice", "age": 30, "city": "New York"}
    person.pop("city")
    print(person)

# Q13. Given two dictionaries, merge them into one
# dict1 = {"a": 1, "b": 2}    dict2 = {"c": 3, "d": 4}

def func13():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict1.update(dict2)
    print(dict1)


def main():
    func1()
    func2()
    func3()
    func4()
    func5()
    func6()
    func7()
    func8()
    func9()
    func10()
    func11()
    func12()
    func13()

main()


