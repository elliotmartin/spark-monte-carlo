import monte_carlo
import random 
from copy import deepcopy

#inspired by https://twitter.com/Monsanto_HS/status/1264981743595118593

lackeys = ["Titanic", "Ethereal", "Kobold", "Draconic", "Goblin", "Faceless", "Witchy"]

def generate_data():
    first_lackey = random.choice(lackeys)
    second_lackey = random.choice(lackeys)
    while first_lackey != "Titanic" and second_lackey != "Titanic":
        first_lackey = random.choice(lackeys)
        second_lackey = random.choice(lackeys)
    return [first_lackey, second_lackey] 

def eval_data(data):
    data = deepcopy(data)
    random.shuffle(data)

    first_lackey = data[0]
    second_lackey = data[1]

    if first_lackey == "Titanic" and second_lackey == "Titanic":
        return True
            
    return False

print(monte_carlo.run_sim(generate_data, eval_data, 5000000))
