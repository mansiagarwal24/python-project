# Q1 Using below list and enumerate(), print index followed by value.
# Input: fruits = ["apple", "banana", "cherry"]
# Output:
#   0 apple
#   1 banana
#   2 cherry
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Q2 Using below dict and enumerate, print key followed by value
#
# Input: person = {"name": "Alice", "age": 30, "city": "New York"}
# Output:
#   name: Alice
#    age: 30
#    city: New York

person = {"name": "Alice", "age": 30, "city": "New York"}

for index, (key, value) in enumerate(person.items()):
    print(f"{key}: {value}")

# Q3 Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples
# where each tuple contains the index and the corresponding fruit, but only for even indices.
# Output:
#   [(2, 'banana'), (4, 'date')]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

result = [(i, fruit) for i, fruit in enumerate(fruits)
          if i % 2 == 0]
print(result)