from random import randint

runs = 1000000
no_para = 0

for a in range(runs):

    options = ['c', 'c', 'c', 'c', 'o', 'o']
    spots = []
    while options != []:
        opt_len = len(options) - 1
        picknum = randint(0, opt_len)
        pick = options.pop(picknum)
        spots.append(pick)

    two_open = list(zip(spots, spots[1:] + spots[:1]))
    two_open = two_open[:4]
    two_open_check = ('o', 'o')
    if spots[5] == 'o':
        no_para += 1
    elif two_open_check in two_open:
        no_para += 1

print(no_para)