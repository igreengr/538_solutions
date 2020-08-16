import random

tests = 1000000
six_len = 0

for a in range(tests):
    ruler = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cut_one = random.uniform(0, 1) * 12
    cut_two = random.uniform(0, 1) * 12
    cut_three = random.uniform(0, 1) * 12
    while cut_one == cut_two:
        cut_two = random.uniform(0, 1) * 12
    while cut_one == cut_three:
        cut_three = random.uniform(0, 1) * 12
    while cut_two == cut_three:
        cut_three = random.uniform(0, 1) * 12

    cuts = [cut_one, cut_two, cut_three]
    cuts.sort()


    ruler_one = [cuts[2], 12]
    ruler_two = [cuts[1], cuts[2]]
    ruler_three = [cuts[0], cuts[1]]
    ruler_four = [0, cuts[0]]

    if cuts[2] < 6:
        len_six = 12 - cuts[2]
        six_len += len_six
    if cuts[1] < 6 and cuts[2] > 6:
        len_six = cuts[2] - cuts[1]
        six_len += len_six
    if cuts[0] < 6 and cuts[1] > 6:
        len_six = cuts[1] - cuts[0]
        six_len += len_six
    if cuts[0] > 6:
        len_six = cuts[0]
        six_len += len_six

avg_six = six_len / tests
print(avg_six)
