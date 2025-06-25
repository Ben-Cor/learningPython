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


#More list practice
number_list = [1, 2, 3, 4, 5]

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_numbers(number_list))
print(sum_numbers([1, 2, 3, -8, 50]))

# Given two integer numbers, write a Python program to return their product only
# if the product is equal to or lower than 1000. Otherwise, return their sum

def product_or_sum(a, b):
    sum = a + b
    product = a * b
    if product > 1000:
        return sum
    else:
        return product

print(product_or_sum(20, 30))  # Should return 600
print(product_or_sum(50, 30))  # Should return 80

#iterate through the first 10 numbers and, in each iteration,
# print the sum of the current and previous number.

def sum_current_previous(number_range):
    for i in range(0, number_range + 1):
        if i == 0:
            print(f"Current Number {i}, Previous Number None, Sum: {i}")
        else:
            print(f"Current Number {i}, Previous Number {i-1}, Sum: {i + (i-1)}")

sum_current_previous(20)