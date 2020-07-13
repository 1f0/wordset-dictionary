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
        print('=' * 20)
        os.system('clear') # for macOS
        print(t)
        for m in j[t]['meanings']:
            for x in m:
                if x != 'id':
                    print('  ', x,':',  m[x])
        yield


if __name__ == '__main__':
    for i in genFlash():
        try:
            time.sleep(5 * 60)
        except:
            try:
                time.sleep(3)
            except:
                print(), exit()
