# Q1 Task: Convert the following values to the specified types and print the results
# 1. Convert 3.75 to an integer and print the value
# 2.Convert "123" to a float and print the value
# 3.Convert 0 to a boolean and print the value
# 4.Convert False to a string and print the value

def q1():
    a=3.75
    print(int(a))
    b="123"
    print(float(b))
    c=0
    print(bool(c))
    d = False
    print(str(d))

# Q2. Convert all characters in the string to uppercase. x = "hello"

def q2(value):
    print(str.upper(value))

# Q3. Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. And convert it to integer.
def q3(x,y):
    z=x+y
    print(z)
    print(type(z))
    print(int(z))


# Q4. Given the string s = 'hello', perform the following operations:
# 1.Convert the string to uppercase.
# 2.Replace 'e' with 'a'.
# 3.Check if the string starts with 'he'.
# 4.Check if the string ends with 'lo'.

def q4(value):
    a= str.upper(value)
    print(a)
    b= str.replace(value,"e","a")
    print(b)
    c= str.startswith(value, "he")
    print(c)
    d=str.endswith(value,"lo")
    print(d)

def main():
    q1()
    q2("hello")
    q3(5,3.14)
    q4("hello")

main()






