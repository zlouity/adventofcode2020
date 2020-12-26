#_test = [int(x) for x in '389125467']
_test = [int(x) for x in '653427918']
#print(_test)
idx = 0
for y in range(100):
    #print("cups",_test)
    _cc = _test[idx]
    #print("current cup", _cc)
    pickup = []
    if y == 8:
        pass
    pos = (idx+1)%len(_test)
    for x in range(3):
        if pos != 0:
            pos = (idx+1)%len(_test)
        pickup.append(_test.pop(pos))
    #print("pickup",pickup)
    dest_cup = None
    possible_idx = _cc-1
    while dest_cup == None:
        if possible_idx in pickup:
            possible_idx -=1
        elif possible_idx == 0:
            possible_idx = max(_test)
        else:
            dest_cup = possible_idx
    #print("dest cup",dest_cup)
    for z in pickup[::-1]:
        _test.insert(_test.index(dest_cup)+1,z)
    idx = (_test.index(_cc)+1) % len(_test)

print("".join([str(x) for x in _test[_test.index(1)+1:]+_test[0:_test.index(1)]]))
        

