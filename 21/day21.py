from collections import defaultdict

_ex = ""

_foods = defaultdict(list)
_ing = []

with open("input.txt") as f:
    _ex = [x.strip().replace('(',"").replace(')',"") for x in f.readlines()]
    
#print(_ex)

for line in _ex:
    _ev = line.split(" contains ")
    alg = _ev[-1].split(", ")
    foods = _ev[0].split()
    #print(alg)
    #print(foods)
    for y in alg:
        _foods[y].append(foods)
    _ing.append(foods)
        
#print(_foods)
det_alg = set()
while len(det_alg) < len(_foods):
    for k,v in _foods.items():
        poss = set(v[0]).intersection(*[set(j) for j in v[1::]])
        poss = poss.difference(det_alg)
        if len(poss) == 1:
            #print(poss)
            det_alg = det_alg.union(poss)

print(det_alg)
counter = 0
for k in _ing:
    non_alg_foods = set(k).difference(det_alg)
    counter += len(non_alg_foods)
    
print(counter)