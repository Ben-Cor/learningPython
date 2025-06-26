
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

# While True loops continue until the condition is false or break is called.
while True:
    word_remove_amount = input(f"Enter how many characters you want to remove from the word (max of {len(word)}): ")
    if not word_remove_amount.isdigit():  # Check if input is a valid number
        print("Please enter a valid number!")
    elif int(word_remove_amount) > len(word):
        print("You can't remove more characters than the word has!")
    else:
        break  # Exit the loop if input is valid

print("Removing characters from your word...")
print(word[:len(word) - int(word_remove_amount)])

number_list = [10, 2, 3, 4, 10]
number_list_2 = [1, 2, 3, 4, 5]

def check_first_and_last_same(numbers):
    first_and_last = True
    if numbers[0] == numbers[len(numbers) - 1]:
        first_and_last = True
    else:
        first_and_last = False
    print(first_and_last)

check_first_and_last_same(number_list) #should be true
check_first_and_last_same(number_list_2) #should be false