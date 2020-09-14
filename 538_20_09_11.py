from random import randint

runs = 5000000
even_teams = 0

for z in range(runs):
    a = randint(1, 5)
    b = randint(1, 5)
    c = randint(1, 5)

    all_teams = [a, b, c]
    all_teams.sort()

    most = all_teams[2]
    others = all_teams[0] + all_teams[1]

    if most == others:
        even_teams += 1

pct = (even_teams / runs) * 100
pct = round(pct, 2)
print(pct, '%')
