import json
import time
import random
import os

def select(w: str) -> bool:
    if len(w) > 5:
        return False
    if ' ' in w or '-' in w:
        return False
    ban_suffix = 'ness', 'ion', 'ian', 'ity', 'able'
    for s in ban_suffix:
        if w.endswith(s):
            return False
    return True


def genFlash():
    with open('data/merge.json') as f:
        dc = json.load(f)
    with open('data/en_US_phon.txt') as f:
        ph_dc = dict(s.split('\t') for s in f.readlines())

    w_list = list(filter(select, dc.keys() & ph_dc.keys()))
    random.shuffle(w_list)

    for w in w_list:
        os.system('clear') # for macOS
        print(w, ph_dc[w])
        for m in dc[w]['meanings'][:3]:
            for x in m:
                if x == 'id':
                    continue
                y = m[x]
                if isinstance(y, list) \
                    and all(isinstance(z, str) for z in y):
                    y = ', '.join(y)
                if x == 'speech_part':
                    x = 'type'
                print(f'  {x}: {y}')
            print()
        yield


if __name__ == '__main__':
    for i in genFlash():
        try:
            time.sleep(5 * 60)
        except:
            try:
                time.sleep(1)
            except:
                print(), exit()
