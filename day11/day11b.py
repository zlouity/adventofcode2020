import numpy as np

directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

def check_gen(r,c,_p):
    x = r
    y = c
    for d in directions:
        x = r + d[0]
        y = c + d[1]
        while 0 <= x < len(_p) and 0 <= y < len(_p[0]):
            
            if _p[x][y] == "#":
                return False
            elif _p[x][y] == "L":
                break
            x+=d[0]
            y+=d[1]
    return True


def check_die(r,c,_p):
    ct = 0
    x = r
    y = c
    for d in directions:
        x = r + d[0]
        y = c + d[1]
        while 0 <= x < len(_p) and 0 <= y < len(_p[0]):
            if _p[x][y] == "#":
                ct +=1
                break
            if _p[x][y] == "L":
                break
            x+=d[0]
            y+=d[1]
    if ct > 4:
        return True
    else:
        return False

def deep_copy(array):
    ret_array = []
    for x in array:
        ret_array.append(x)
    return ret_array

def gen(_p):
    new = []
    for v,x in enumerate(_p):
        line = ""
        for t,y in enumerate(x):
            if y == "L":
                if check_gen(v,t,_p):
                    line += "#"
                else:
                    line += "L"
            elif y == "#":
                if check_die(v,t,_p):
                    line += "L"
                else:
                    line +="#"
            else:
                line += "."
        new.append(line)
    return new

def check(old,new):
    count =0
    for v,x in enumerate(old):
        if x != new[v]:
            return -1
        else:
            count += x.count("#")
    return count
    

with open("input.txt") as f:
    _p = []
    for line in f.readlines():
        _p.append(line.strip())
    print("\n".join(_p))
    print(len(_p[0]))
    _a = np.array(_p)
    count = -1
    #print("test")
    #print("\n".join(gen(_p)))
    while count == -1:
        #print("new gen")
        n = deep_copy(gen(_p))
        count = check(_p, n)
        _p = deep_copy(n)
        print(count)
        print("\n".join(_p))
    print("\n".join(n))
    print(count)
    