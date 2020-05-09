import random
import os


ileCyfr = 6
lowestValue = 1
highestValue = 49


class lotto(object):
    cyfry = []    
    def losuj(min, max):
        return random.randint(min, max)
    
    def proces(ist):
        for i in range(ist):
            lotto.cyfry.append(lotto.losuj(lowestValue, highestValue))
            while lotto.cyfry[i] in lotto.cyfry[:i]:
                lotto.cyfry[i] = lotto.losuj(lowestValue, highestValue)
        
        
        return lotto.cyfry

lotto.proces(ileCyfr)
lotto.cyfry.sort()
os.system('cls' if os.name == 'nt' else 'clear')
print(lotto.cyfry)
