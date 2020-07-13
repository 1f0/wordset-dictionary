import json
import time
import random
import os


def genFlash():
    with open('data/merge.json') as f:
        j = json.load(f)
    k = list(j.keys())
    random.shuffle(k)
    for t in k:
        os.system('clear') # for macOS
        print(t)
        for m in j[t]['meanings']:
            for x in m:
                if x != 'id':
                    print('  ', x,':',  m[x])
            yield

flash = genFlash()


if __name__ == '__main__':
    while True:
        try:
            next(flash)
            time.sleep(3 * 60)
        except KeyboardInterrupt:
            next(flash)
            n = 5
            print(f'; Wanna exit? Ctrl-C again in {n}s.')
            try:
                time.sleep(n)
            except KeyboardInterrupt:
                print()
                exit()
