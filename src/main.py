# Testing the int function in Python to convert a string to an integer
age = int("36")

greeting = f"Hello, I am Ben and I am {age} years old"
print(greeting)

# This is a comment in python

for i in range(5):
    print(5-i)
print("Blast Off!")


if age > 30:
    print("You are over 30 years old")
elif age > 18:
    print("You are over 18 years old")
else:
    print("You are under 18 years old")

# fizzbuzz
# count up from one, replacing multiples of three with "Fizz",
# multiples of five with "Buzz",
# and multiples of both with "FizzBuzz"

fizz_buzz_start = 1
fizz_buzz_end = 100
fizz_buzz_list = []

for i in range(fizz_buzz_start, fizz_buzz_end + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        fizz_buzz_list.append ("FizzBuzz")
    elif i % 5 == 0:
        fizz_buzz_list.append ("Buzz")
    elif i % 3 == 0:
        fizz_buzz_list.append ("Fizz")
    else:
        fizz_buzz_list.append(i)

for item in fizz_buzz_list:
    print(item)

# Functions
def greet(name):
    return f"Hello, I am {name}!"

print (greet("Ben"))