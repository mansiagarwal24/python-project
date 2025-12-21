# Q1 . Write a Python program to read the entire content of a file named sample.txt and display it.

with open("file.txt", "r") as file:
    content = file.read()
    print(content)


# Q2. Write a Python program to count the number of words in a file named words.txt

count = 0
with open("output.txt", "r") as file:
    for line in file:
        words = line.split()
        count += len(words)

print("Total word count:", count)


# Q3.Create a program to write the string “Hello, Python!” into a file named output.txt.
with open("output.txt", "w") as file:
    file.write("Hello, Python!")


# Q4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries
#
# 	data = [
#     ["Name", "Roll Number", "Marks"],
#     ["Alice", "101", "85"],
#     ["Bob", "102", "90"],
#     ["Charlie", "103", "88"]
# ]
import csv

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("students.csv created successfully!")

# Q5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
def read_file_generator(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line.strip()

for row in read_file_generator("file.txt"):
    print(row)