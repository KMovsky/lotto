import random
import os


ileCyfr = 6
lowestValue = 1
highestValue = 49


class lotto(object):
    cyfry = []

    def proces(ist):
        lotto.cyfry = random.sample(range(lowestValue, highestValue),ist)
        return lotto.cyfry

lotto.proces(ileCyfr)
lotto.cyfry.sort()
os.system('cls' if os.name == 'nt' else 'clear')
print(lotto.cyfry)
