from random import randint

runs = 1000000
d = 0
m = 0
for a in range(runs):
    bag = ['d', 'd', 'd', 'm', 'd', 'd', 'd', 'm', 'd', 'd']
    picknum = 0
    while bag != []:
        if picknum == 0:
            bag_len = len(bag) - 1
            pick = randint(0, bag_len)
            first_pick = bag.pop(pick)
            picknum += 1
            prev_pick = first_pick
        else:
            bag_len = len(bag) - 1
            pick = randint(0, bag_len)
            curr_pick = bag[pick]
            if curr_pick == prev_pick:
                prev_pick = bag.pop(pick)
                bag_len = len(bag) - 1
            else:
                picknum = 0
    if curr_pick == 'd':
        d += 1
    elif curr_pick == 'm':
        m += 1
print(d, m)
