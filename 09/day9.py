from itertools import combinations

def check(num, _l):
    temp = [x[0]+x[1] for x in combinations(_l,2)]
    if num not in temp:
        print(num)
        return num
    else:
        return -1
pre = 25
with open("input.txt") as f:
    _p = []
    for line in f.readlines():
        _p.append(int(line.strip()))
    ans = 0
    for t in range(pre,len(_p)):
        ans = check(_p[t],_p[t-pre:t])
        if ans>0:
            break
        
        
