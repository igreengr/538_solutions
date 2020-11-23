import random
from collections import Counter

runs = 5000000
final_sauce = []

for run in range(runs):

    has_sauce = 1

    got_sauce = [1]
    got_sauce_len = len(got_sauce)

    while got_sauce_len != 20:
        x = random.uniform(0, 1)

        if x <= .5:
            pass_dir = -1
        else:
            pass_dir = +1

        has_sauce += pass_dir

        if has_sauce == 0:
            has_sauce = 20

        if has_sauce == 21:
            has_sauce = 1

        if has_sauce not in got_sauce:
            got_sauce.append(has_sauce)
        got_sauce_len = len(got_sauce)

    last_sauce = got_sauce[19]
    final_sauce.append(last_sauce)

count = Counter(final_sauce)

# most = count.most_common(count)
print(count)
