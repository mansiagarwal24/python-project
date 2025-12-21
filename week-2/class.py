# Q1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = Person("John",18)
print(person1.age)
print(person1.name)

print('{} {}'.format(person1.name,person1.age))


# Q2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
#
class BankAccount:

    def __init__(self, account_number,balance,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print( "After deposit {} :".format(amount), self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print( "After withdraw {} :".format(amount) , self.balance)

    def check_balance(self):
        print( "your current balance is :", self.balance)


account1 = BankAccount(23456, 4500,"Mansi")
account1.check_balance()
account1.withdraw(300)
account1.check_balance()
account1.deposit(2000)
account1.check_balance()

# Q3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
#
#       book = Book.from_string("Python Programming, John Doe")
#
# Q4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
d.sound()

c = Cat()
c.sound()

# Q5. Write a code to perform multiple inheritance.

class Shapes:
    def area(self):
        print (8 * 4)


class Triangle:
    def area(self):
        print (4 * 5)


class Cone(Shapes, Triangle):
    pass

c = Cone()
c.area()




