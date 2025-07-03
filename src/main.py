# # 8 ball code
#
# name = input("Hello, what is your name?")
# while name == "":
#     name = input("You didn't enter a name, please enter your name: "
#                  "If you wish to exit, please type exit and press enter: ")
# if name.lower() == "exit":
#     print("Goodbye!")
#     exit()
#
#
# question = input(f"Hello {name}. What question do you want to ask the 8 ball? ")
# while question == "":
#     question = input(f"You didn't ask a question, {name}. Please ask a question for the 8 ball. "
#                      "If you wish to exit, please type exit and press enter: ")
# if question.lower() == "exit":
#     print("Goodbye!")
#     exit()
#
# import random
# random_number = random.randint(1, 9)
#
# match random_number:
#     case 1:
#         answer = "Yes - definitely."
#     case 2:
#         answer = "It is decidedly so."
#     case 3:
#         answer = "Without a doubt."
#     case 4:
#         answer = "Reply hazy, try again."
#     case 5:
#         answer = "Ask again later."
#     case 6:
#         answer = "Better not tell you now."
#     case 7:
#         answer = "My sources say no."
#     case 8:
#         answer = "Outlook not so good."
#     case 9:
#         answer = "Very doubtful."
#     case default :
#         answer = "Error: Invalid response."
#
# print(f"{name}, you asked - {question}. The 8 ball says: {answer}")
#
#
# weight = input("How much does your parcel weigh?")
#
# while True:
#     if weight.lower() == "exit":
#         print("Goodbye!")
#         exit()
#
#     # Check if it's a valid number (either integer or float)
#     try:
#         # Try to convert to float
#         weight_float = float(weight)
#         weight = weight_float
#         break  # Exit the loop if conversion succeeds
#     except ValueError:
#         # If conversion fails, ask for input again
#         weight = input("Invalid input. Please enter a valid weight (number), or type 'exit' to quit: ")
#
# cost = 0
# # Ground shipping
# if weight <= 2:
#   cost = (weight * 1.5) + 20
# elif weight <= 6:
#   cost = (weight * 3) + 20
# elif weight <= 10:
#   cost = (weight * 4) + 20
# else:
#   cost = (weight * 4.75) + 20
#
# print(f"Total cost (Ground) = ${cost:.2f}")
# #premium is a flat rate
# print("Premium cost (Ground) = $125")
#
# #Drone Shipping
#
# drone_cost = 0
# if weight <= 2:
#   drone_cost = (weight * 4.5)
# elif weight <= 6:
#   drone_cost = (weight * 9)
# elif weight <= 10:
#   drone_cost = (weight * 12)
# else:
#   drone_cost = (weight * 14.25)
#
# print(f"Total cost (Drone) = ${drone_cost:.2f}")

# loops practice
def tenth_power(num):
  return num ** 10

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))

def square_root(num):
  return num ** 0.5

print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

def win_percentage(wins, losses):
  games = wins + losses
  return wins / (games/100)

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

def average(num1, num2):
  return (num1 + num2)/2

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

def remainder(num1, num2):
  return (num1 * 2) % (0.5 * num2)

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

def first_three_multiples(num):
  for i in range(1, 4):
    print(num*i)
  return num*3

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0