def inv(n,x):
    for thing in range(x):
        if (thing*n)%x==1:
            return thing

with open("input.txt") as f:
    _p = []
    for x in f.readlines():
        _p.append(x)
    _i = int(_p[0].strip())
    _t = [int(r) for r in _p[1].strip().replace(",x",",-1").split(",")]
    _n = _t.copy()
    print(_n)
    _b = []
    total = 1
    for v,x in enumerate(_n):
        if x != -1:
            _b.append([x,(x-v)%x])
            total *= x
    print(_b)
    print(total)
    for thing in _b:
        thing.append(int(total/thing[0]))
    for thing in _b:
        thing.append(inv(thing[-1],thing[0]))
    print(sum([i[1]*i[2]*i[3] for i in _b])%total)  