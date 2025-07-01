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

#functions practice
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = (hotel_rate * trip_time) - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  return trip_total

print(calculate_expenses(200, 100, 100, 5))

#arguments practice
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print(f"First, we will stop in {first_destination}, then {second_destination} and lastly {final_destination}")

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
trip_planner("Brooklyn", "Queens")

#built in functions practice
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)

print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)

print(min_price)

rounded_price = round(tshirt_price, 1)
print(rounded_price)

#function further practice
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below:

def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

#multiple returns
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)


#function practice test
#tripplanner welcome function created
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Ben")

#estimated time function created
def estimated_time_rounded(estimated_time):
  if estimated_time > 0:
    rounded_time = round(estimated_time)
    return rounded_time
  else:
    print("Please supply a time greater than 0")

estimate = estimated_time_rounded(2.5)

#destination_setup created
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print(f"It will take approximately {estimated_time} hours")

destination_setup("Bath", "London", estimate)

estimate = estimated_time_rounded(1.25)
destination_setup("Bath", "Bristol", estimate, "Bike")

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#farenheit to celcuis function
def f_to_c(f_temp):
  c_temp = (f_temp-32)* 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

#celcius to farenheit function
def c_to_f(c_temp):
  f_temp = c_temp* (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

# function to calculate force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print(f"The GE train supplies {train_force} Newtons of force.")

#get energy function
def get_energy(mass, c = (3*10**8)):
  return mass * (c ** 2)

bomb_energy = get_energy(bomb_mass)

print(f"A 1kg bomb supplies {bomb_energy} Joules")

#get work function
def get_work(mass, acceleration, distance):
  return (get_force(mass, acceleration))*distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")