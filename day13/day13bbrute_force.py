with open("test.txt") as f:
    _p = []
    for x in f.readlines():
        _p.append(x)
    _i = int(_p[0].strip())
    _t = [int(r) for r in _p[1].strip().replace(",x",",-1").split(",")]
    _n = _t.copy()
#     print(_i)
#     print(_t)
#     print(_n)
    _f = True
    _ti = 0
    while _f:
#         print(_n)
#         if _ti % 1000000000 == 0:
#                 print(_ti)
#                 print(_n)
        for v,x in enumerate(_n):
#             if _ti == 3417:
#                 input()
            if x-_ti != v:
                _f = False
        if _f:
            print(_ti)
            _f = False
        else:
            _f = True
            _min = _n[0]+_t[0]
            _last = _min
            for v,x in enumerate(_n):
                if x!= -1:
                    while(_n[v] < _last):
                        _n[v] +=_t[v]
                    _last = _n[v]
        _ti = _min
        print(_ti)
        print(_n)