from random import randint

runs = 1000000
grand_tot = 0

for run in range(runs):
    dd = randint(0, 29)
    q_vals = [200, 200, 200, 200, 200, 200, 400, 400, 400, 400, 400, 400, 600, 600, 600, 600, 600, 600, 800, 800, 800, 800,
              800, 800, 1000, 1000, 1000, 1000, 1000, 1000]

    tot = 0
    cur_q = 0
    q_vals_len = len(q_vals) - 1
    while q_vals != []:
        pick_q = randint(0, q_vals_len)

        cur_val = q_vals.pop(pick_q)
        if cur_q == dd:
            if tot <= 1000:
                tot = tot + 1000
            else:
                tot = tot * 2
        else:
            tot += cur_val
        cur_q += 1
        q_vals_len = len(q_vals) - 1
    grand_tot += tot

avg = grand_tot / runs
print(avg)
