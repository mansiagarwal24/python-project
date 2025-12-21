# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10  numbers

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))

# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
#   Input n=3

def infinite_multiples(n):
    i = 1
    while True:
        yield n * i
        i += 1

gen = infinite_multiples(3)
for _ in range(10):
    print(next(gen))

# 3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
#
# word = “hello”
# times = 5
def repeat_word(word, times):
    for _ in range(times):
        yield word

for w in repeat_word("hello", 5):
    print(w)