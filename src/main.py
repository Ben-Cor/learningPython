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
    return f"Hello, from {name}!"

print (greet("Ben"))

# Function with variable number of arguments
def greet_2(*name):
    return f"Hello, from {name[2]}!"

print (greet_2("Ben", "Sian", "Sweep"))

# Function with keyword arguments
def dog_name(dog1, dog2, dog3):
    print (f"My dog is {dog1}")

dog_name(dog1="Sweep", dog2="Lassie", dog3="Spot")

#function with positional and kwargs

def person_info(job_title, name, age):
    print(f"{name} is a {job_title} and is {age} years old.")

person_info("Software Engineer", age=36, name="Ben")