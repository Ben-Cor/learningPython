import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_year = dt.datetime.now().year
current_time = dt.datetime.now().time
print(f"It is currently {current_year}")

#generate target year
target_year = randint(1066, 2020)
#initial list of destinations
destinations_list = ["England", "America", "India"]
#choose destination
destination = choice(destinations_list)

#calculate cost to 2 dp
cost = Decimal(0.55) * (current_year - target_year)
TWOPLACES = Decimal("0.01")
cost = cost.quantize(TWOPLACES)

print(custom_module.generate_time_travel_message(year=target_year, destination = destination, cost = cost))