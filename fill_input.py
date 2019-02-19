
#   Fills input file with random numbers    #

import os
from random import randint

def fill():
    if os.path.exists('ARAB.IN'):
        with open('ARAB.IN', 'w') as f:
            for i in range(30):
                f.write(str(randint(0, 4000)) + '\n')
    else:
        print('\nFile not found!')