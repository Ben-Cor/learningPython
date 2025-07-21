import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_year = dt.datetime.now().year
current_time = dt.datetime.now().time
print(current_year)

def cost_calculate(target_year):
  cost = Decimal(0.55) * (current_year - target_year)
  TWOPLACES = Decimal("0.01")
  return cost.quantize(TWOPLACES)

print(cost_calculate(1965))