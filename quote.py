import pandas as pd
from time import sleep
from random import shuffle
import random
import os
txt = pd.read_csv('data/quotes.csv').title
shuffle(txt)
w, h = os.get_terminal_size()
c = h // 2 - 2
for t in txt:
    if not isinstance(t, str):
        continue
    os.system('clear')
    print('\n'*c, t.center(w),'\n'*c)
    try:
        sleep(60 * 10)
    except:
        try:
            sleep(1)
        except:
            exit()

