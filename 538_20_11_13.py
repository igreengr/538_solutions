from random import randint

runs = 1000000
grand_tot = 0

for run in range(runs):
    dd = randint(0, 29)
    q_vals = [200, 200, 200, 200, 200, 200, 400, 400, 400, 400, 400, 400, 600, 600, 600, 600, 600, 600, 800, 800, 800, 800,
              800, 800, 1000, 1000, 1000, 1000, 1000, 1000]

    tot = 0
    cur_q = 0
    while q_vals != []:
        cur_val = q_vals.pop(0)
        if cur_q == dd:
            if tot <= 1000:
                tot = tot + 1000
            else:
                tot = tot * 2
        else:
            tot += cur_val
        cur_q += 1
    grand_tot += tot

avg = grand_tot / runs
print(avg)
