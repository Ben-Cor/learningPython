
#More list practice
number_list = [1, 2, 3, 4, 5]

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Given two integer numbers, write a Python program to return their product only
# if the product is equal to or lower than 1000. Otherwise, return their sum

def product_or_sum(a, b):
    sum = a + b
    product = a * b
    if product > 1000:
        return sum
    else:
        return product

#iterate through the first 10 numbers and, in each iteration,
# print the sum of the current and previous number.

def sum_current_previous(number_range):
    for i in range(0, number_range + 1):
        if i == 0:
            print(f"Current Number {i}, Previous Number None, Sum: {i}")
        else:
            print(f"Current Number {i}, Previous Number {i-1}, Sum: {i + (i-1)}")


word = input("Enter your word:")
print("Printing only even characters...")
for i in range(len(word)):
    if i % 2 == 0:
        print(word[i])