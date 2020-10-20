from random import random

runs = 1000000
runoffs = 0

for run in range(runs):
    a = random()
    b = random()
    c = random()

    d = a + b + c

    e = 1 / d

    a = a * e
    b = b * e
    c = c * e

    if a < .5 and b < .5 and c < .5:
        runoffs += 1

print(runoffs)
