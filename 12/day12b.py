with open("input.txt") as f:
    _p = []
    _c = [10,1]
    _pn = [0,0]
    for line in f.readlines():
        _p.append(line.strip())
    for x in _p:
        if x[0] == "F":
            _pn[0] += _c[0]*int(x[1:])
            _pn[1] += _c[1]*int(x[1:])
        elif x[0] == "N":
            _c[1] += int(x[1:])
        elif x[0] == "S":
            _c[1] -= int(x[1:])
        elif x[0] == "E":
            _c[0] += int(x[1:])
        elif x[0] == "W":
            _c[0] -= int(x[1:])
        elif x[0] == "L":
            _f = (int(x[1:])//90)%4
            t1= _c[0]
            t2= _c[1]
            if _f == 1:
                _c = [-t2,t1]
            elif _f ==2:
                _c = [-t1,-t2]
            elif _f ==3:
                _c = [t2,-t1]
        elif x[0] == "R":
            _f = (int(x[1:])//90)%4
            t1= _c[0]
            t2= _c[1]
            if _f == 1:
                _c = [t2,-t1]
            elif _f ==2:
                _c = [-t1,-t2]
            elif _f ==3:
                _c = [-t2,t1]
        print(_pn)
    print(abs(_pn[0])+abs(_pn[1]))