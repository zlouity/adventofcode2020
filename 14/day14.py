
def _bin(num):
    _ret = ""
    while num >0:
        if num % 2 == 0:
            _ret = "0" + _ret
        else:
            _ret = "1"+_ret
        num = num // 2
    #print(_ret)
    _l = len(_ret)
    if _l < 36:
        _ret  = ("0"*(36-_l))+_ret
    return _ret

def _mask(_m,b):
    _ret = ""
    _two = _bin(b)
    for i,j in enumerate(_m):
        if j != "X":
            _ret += j
        else:
            _ret += _two[i]
    return(int(_ret,2))
    

#print(_bin(73))

with open("input.txt") as f:
    mem = {}
    _p = []
    curr_mask = 0
    for line in f.readlines():
        _p.append(line.strip())
    
    for x in _p:
        if "mask" in x:
            curr_mask = x.split("=")[1].strip()
            print(curr_mask)
        elif "mem" in x:
            add = x.split("=")[0]
            add = int(add[add.index("[")+1:add.index("]")])
            
            _n = int(x.split("=")[1].strip())
            _mn = _mask(curr_mask,_n)
            print(_mn)
            mem[add] = _mn
        
    print(mem)
    print(sum([v for x,v in mem.items()]))
            #print(_n)
            #print(x.split("="))
            #print("mem",x)