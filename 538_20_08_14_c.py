from random import randint

tests = 1000000
six_len = 0

for a in range(tests):
    ruler = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cut_one = randint(1, 11)
    cut_two = randint(1, 11)
    cut_three = randint(1, 11)
    while cut_one == cut_two:
        cut_two = randint(1, 11)
    while cut_one == cut_three:
        cut_three = randint(1, 11)
    while cut_two == cut_three:
        cut_three = randint(1, 11)

    cuts = [cut_one, cut_two, cut_three]
    cuts.sort()
    ruler_one = ruler[0:cuts[0]]
    ruler_two = ruler[cuts[0]:cuts[1]]
    ruler_three = ruler[cuts[1]:cuts[2]]
    ruler_four = ruler[cuts[2]:]
    # print(ruler_one, ruler_two, ruler_three, ruler_four)
    if 6 in ruler_one:
        six_len += len(ruler_one)
    elif 6 in ruler_two:
        six_len += len(ruler_two)
    elif 6 in ruler_three:
        six_len += len(ruler_three)
    elif 6 in ruler_four:
        six_len += len(ruler_four)

avg_six = six_len / tests
print(avg_six)