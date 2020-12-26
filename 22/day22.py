with open('input.txt') as f:
    _p1_d  = [int(x.strip()) for x in f.readlines()]

with open('input2.txt') as f:
    _p2_d = [int(x.strip()) for x in f.readlines()]


def _round(_p1_d,_p2_d):
    t1 = _p1_d.pop(0)
    t2 = _p2_d.pop(0)
    if t1 > t2:
        _p1_d.append(t1)
        _p1_d.append(t2)
    else:
        _p2_d.append(t2)
        _p2_d.append(t1)


while len(_p1_d) > 0 and len(_p2_d) > 0:
    _round(_p1_d,_p2_d)
    
print(_p1_d)
print(_p2_d)

score = 0
if len(_p1_d) >0:
    for x,v in enumerate(_p1_d[::-1]):
        score+=(x+1)*v
else:
    for x,v in enumerate(_p2_d[::-1]):
        score+=(x+1)*v

print(score)