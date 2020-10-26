from random import random
from random import randint

runs = 100000
shots = 100
pick_is_make = 0
sets = []

for run in range(runs):
    sets = []
    for shot in range(shots):
        results = []

        for attempts in range(3):
            attempt = random()
            if attempt < .5:
                results.append('y')
            else:
                results.append('n')

        shot_a = results[0]
        shot_b = results[1]

        if shot_a == 'y' or shot_b == 'y':
            sets.append(results)

    sets_len = len(sets) - 1
    pick_set = randint(0, sets_len)
    picked_set = sets[pick_set]

    prev_make = False

    while prev_make == False:
        pick_shot = randint(1, 2)
        prev_shot = pick_shot - 1
        picked_shot = picked_set[pick_shot]
        is_prev_make = picked_set[prev_shot]
        if is_prev_make == 'y':
            prev_make = True
    if picked_shot == 'y':
        pick_is_make += 1

print(pick_is_make)