translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

animals_in_zoo = {}
animals_in_zoo["zebras"]=8
animals_in_zoo["monkeys"]=12
animals_in_zoo["dinosaurs"]=0
print(animals_in_zoo)

#adding multiple values at once with update
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#overwriting values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"]="Viola Davis"
oscar_winners["Best Picture"]="Moonlight"

#zipped lists
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}