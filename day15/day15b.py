_p = [0,1,5,10,3,12,19]
_a = {}
for v,x in enumerate(_p):
    _a[x] = [v]
print(_a)
last = _p[-1]
new_last = 0
for i in range(len(_p),30000000):
    if len(_a[last]) > 1:
        new_last = _a[last][1]-_a[last][0]
    else:
        new_last = 0
    if new_last not in _a:
        _a[new_last] = [i]
    _a[new_last].append(i)
    if len(_a[new_last]) > 2:
        _a[new_last].pop(0)
    
    last = new_last
    
    if i % 1000000 == 0:
        print(i)

print(last)
    