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

# strings practice

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[0:3] + last_name[0:3]
  return account_name

new_account = account_generator(first_name, last_name)