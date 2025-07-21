import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_year = dt.datetime.now().year
current_time = dt.datetime.now().time
print(current_year)

def cost_calculate(target_year):
  return Decimal(0.55) * (current_year - target_year)

print(cost_calculate(1965))