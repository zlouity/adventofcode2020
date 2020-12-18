with open("input.txt") as f:
    _p = []
    for x in f.readlines():
        _p.append(x)
    _i = int(_p[0].strip())
    _t = [int(r) for r in _p[1].strip().replace(",x","").split(",")]
    _n = _t.copy()
    _min = 9999999999999999999999999999999999999999
    _minid = 0
    print(_i)
    print(_t)
    while sum([1 for x in _n if x > _i]) < len(_t):
        for v,u in enumerate(_n):
            if u > _i:
                if u < _min:
                    _min = u
                    _minid = _t[v]
            else:
                _n[v] +=_t[v]
    print(_min,_i,_minid)
    print((_min-_i)*_minid)
    
    