from itertools import combinations
def _case(n, _i,_m):
    b = set(_i).difference(set(_m))
    if len(b)==3:
        return 7
    elif len(b) == 2:
        return 4
    elif len(b) == 1:
        return 2
    else:
        return 1


with open("input.txt") as f:
    _p = []
    for line in f.readlines():
        _p.append(int(line.strip()))
    _p.sort()
    _p.insert(0,0)
    _p.append(_p[-1]+3)
    #print(_p)
    total = 1
    mando = []
    x = 1
    while x < len(_p):
        if _p[x]-_p[x-1] ==3:
            mando.append(_p[x-1])
            mando.append(_p[x])
        x +=1
    mando.append(_p[-1])
    mando.append(0)
    mando = list(set(mando))
    mando.sort()
    #print(mando)
    x = 0
    while x < len(_p):
        num = _p[x]
        start = x
        x+=1
        while x < len(_p) and _p[x] <=num+3:
            x+=1
        total= total*_case(num,_p[start:x],mando)
    print(total) 