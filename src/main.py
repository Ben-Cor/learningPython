# 8 ball code

name = input("Hello, what is your name?")
while name == "":
    name = input("You didn't enter a name, please enter your name: "
                 "If you wish to exit, please type exit and press enter: ")
if name.lower() == "exit":
    print("Goodbye!")
    exit()


question = input(f"Hello {name}. What question do you want to ask the 8 ball? ")
while question == "":
    question = input(f"You didn't ask a question, {name}. Please ask a question for the 8 ball. "
                     "If you wish to exit, please type exit and press enter: ")
if question.lower() == "exit":
    print("Goodbye!")
    exit()

import random
random_number = random.randint(1, 9)

match random_number:
    case 1:
        answer = "Yes - definitely."
    case 2:
        answer = "It is decidedly so."
    case 3:
        answer = "Without a doubt."
    case 4:
        answer = "Reply hazy, try again."
    case 5:
        answer = "Ask again later."
    case 6:
        answer = "Better not tell you now."
    case 7:
        answer = "My sources say no."
    case 8:
        answer = "Outlook not so good."
    case 9:
        answer = "Very doubtful."
    case default :
        answer = "Error: Invalid response."

print(f"{name}, you asked - {question}. The 8 ball says: {answer}")


weight = input("How much does your parcel weigh?")

while weight == "" or not weight.isdigit():
    weight = input("You didn't enter a weight, please enter the weight of your parcel: "
                   "If you wish to exit, please type exit and press enter: ")

if weight.lower() == "exit":
    print("Goodbye!")
    exit()

cost = 0
# Ground shipping
if int(weight) <= 2:
  cost = (int(weight) * 1.5) + 20
elif int(weight) <= 6:
  cost = (int(weight) * 3) + 20
elif int(weight) <= 10:
  cost = (int(weight) * 4) + 20
else:
  cost = (int(weight) * 4.75) + 20

print(f"Total cost (Ground) = ${cost}")
#premium is a flat rate
print("Premium cost (Ground) = $125")

#Drone Shipping

dront_cost = 0
if int(weight) <= 2:
  drone_cost = (int(weight) * 4.5)
elif int(weight) <= 6:
  drone_cost = (int(weight) * 9)
elif int(weight) <= 10:
  drone_cost = (int(weight) * 12)
else:
  drone_cost = (int(weight) * 14.25)

print(f"Total cost (Drone) = ${drone_cost}")