with open("input.txt") as f:
    _p = []
    _d = {"N":[0,1], "E":[1,0],"S":[0,-1],"W":[-1,0]}
    _d2 = ["N", "E","S","W"]
    _f = 1
    _c = [0,0]
    for line in f.readlines():
        _p.append(line.strip())
    for x in _p:
        if x[0] == "F":
            _c[0] += _d[_d2[_f]][0]*int(x[1:])
            _c[1] += _d[_d2[_f]][1]*int(x[1:])
        elif x[0] == "N":
            _c[1] += int(x[1:]) 
        elif x[0] == "S":
            _c[1] -= int(x[1:]) 
        elif x[0] == "E":
            _c[0] += int(x[1:])
        elif x[0] == "W":
            _c[0] -= int(x[1:])
        elif x[0] == "L":
            _f = (_f - ((int(x[1:]) // 90)))%4
        elif x[0] == "R":
            _f = (_f + ((int(x[1:]) // 90)))%4
    print(abs(_c[0])+abs(_c[1]))