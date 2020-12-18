def _bin(num,bits=36):
    _ret = ""
    while num >0:
        if num % 2 == 0:
            _ret = "0" + _ret
        else:
            _ret = "1"+_ret
        num = num // 2
#     _l = len(_ret)
#     if _l < bits:
#         _ret  = ("0"*(bits-_l))+_ret
    return _ret.zfill(bits)
def _mask(_m,b):
    _ret = ""
    _two = _bin(b)
    for i,j in enumerate(_m):
        if j == "X":
            _ret += "X"
        elif j == "1":
            _ret += j
        else:
            _ret += _two[i]
    return(_ret)
def _fa(_r):
    _ret = []
    _x = []
    for i,j in enumerate(_r):
        if j == "X":
           _x.append(i)
    for j in range(2**len(_x)):
        _curr = _bin(j,len(_x))
        for z,v in enumerate(_x):
            _t = list(_r)
            _t[v] = _curr[z]
            _r = "".join(list(_t))
        _ret.append(int(_r,2))
    return _ret
with open("input.txt") as f:
    mem = {}
    _p = []
    curr_mask = 0
    for line in f.readlines():
        _p.append(line.strip())
    for x in _p:
        if "mask" in x:
            curr_mask = x.split("=")[1].strip()
        elif "mem" in x:
            add = x.split("=")[0]
            add = int(add[add.index("[")+1:add.index("]")])
            _n = int(x.split("=")[1].strip())
            for u in set(_fa(_mask(curr_mask,add))):
                mem[u] = _n    
    print(mem)
    print(sum([v for x,v in mem.items()]))