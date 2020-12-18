_p = [0,1,5,10,3,12,19]
#_p = [0,3,6]
_a = {}
for v,x in enumerate(_p):
    _a[x] = [v]
print(_a)
for i in range(len(_p),30000000):
    if _p[i-1] in _p[0:i-1]:
        _p.append(_a[_p[i-1]][-1]-_a[_p[i-1]][-2])
        
        if _p[-1] not in _a:
            _a[_p[-1]] = [i]
        else:
            _a[_p[-1]].append(i)
    else:
        _p.append(0)
        _a[0].append(i)
    
    if i % 1000000 == 0:
        print(i)

print(len(_p))
print(_p[-1])
    