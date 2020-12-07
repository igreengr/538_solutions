from random import randint

runs = 1000000
no_self_pick = 0

for run in range(runs):
    fail = 0

    pickers = ['AJ', 'BJ', 'CJ', 'DJ', 'EJ']
    picks = ['AJ', 'BJ', 'CJ', 'DJ', 'EJ']

    for picker in pickers:
        picks_len = len(picks) - 1
        pick_spot = randint(0, picks_len)
        pick = picks.pop(pick_spot)
        if pick == picker:
            fail += 1

    if fail == 0:
        no_self_pick += 1

pct = (no_self_pick / runs) * 100
print(pct)
