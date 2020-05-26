import random
from copy import deepcopy
import monte_carlo

#inspired by https://twitter.com/Monsanto_HS/status/1265277979590041600
def generate_deck():
    deck = ["x"] * 29
    deck.append("m")
    return deck

def sim_once(deck):
    random.shuffle(deck)
    deck = deepcopy(deck)
    hand = []
    for i in range(5):
        random.shuffle(deck)
        hand.append(deck.pop())


    played = []
    for i in range(20):
        random.shuffle(deck)
        played.append(deck.pop())

    random.shuffle(deck)

    return deck[0] == "m"

def sim_n(n):
    success = 0
    for i in range(n):
        if sim_once():
            success += 1
    return success/n

print(monte_carlo.run_sim(generate_deck, sim_once, 500000))
