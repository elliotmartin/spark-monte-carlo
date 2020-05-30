import monte_carlo
import random

#inspired by https://twitter.com/TicTac_HS/status/1266774348398047232
def generate_data():
    if random.randint(0,99) < 3:
        bots_popped = 5
    else:
        bots_popped = 6
    dmg_face = 0
    dmg_dw = 0
    for i in range(bots_popped):
        dmg = random.randint(1,4)
        to_dmg = random.choice(['dw', 'face'])
        if to_dmg == "dw":
            dmg_dw += dmg
        else:
            dmg_face += dmg
    return((dmg_face, dmg_dw))

def eval_data(dmg_dealt):
    if dmg_dealt[1] >= 9:
        return True
    return False

print(monte_carlo.run_sim(generate_data, eval_data, 500000))
