import json
d = dict()
for i in range(26):
    c = chr(ord('a')+i)
    s = c + '.json'
    with open(s) as f:
        j = json.load(f)
        d.update(j)

with open('merge.json', 'w') as f:
    json.dump(d, f)
