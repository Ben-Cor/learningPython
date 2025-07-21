import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_year = dt.datetime.now().year
current_time = dt.datetime.now().time
print(current_year)

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

print(destination)