with open("input.txt") as f:
    _p = []
    one = 0
    three = 0
    for line in f.readlines():
        _p.append(int(line.strip()))
    _p.sort()
    print(_p)
    if _p[0] == 1:
        one+=1
    elif _p[0] == 3:
        three+=1
    for x in range(len(_p)-1):
        if (_p[x+1] - _p[x]) == 1:
            one+=1
        elif (_p[x+1] - _p[x]) == 3:
            three+=1
    print(one,three+1)
    print(one*(three+1))
        
