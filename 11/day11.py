import numpy as np

def check_gen(r,c,_p):
    sr = max(0,r-1)
    er = min(r+2, len(_p))
    sc = max(0,c-1)
    ec = min(len(_p[0]),c+2)
    for row in range(sr,er):
        for col in range(sc,ec):
            if _p[row][col] == "#":
                if row == r and col == c:
                    pass
                else:
                    return False
    return True


def check_die(r,c,_p):
    sr = max(0,r-1)
    er = min(r+2, len(_p))
    sc = max(0,c-1)
    ec = min(len(_p[0]),c+2)
    ct = 0
    for row in range(sr,er):
        for col in range(sc,ec):
            #print("checking",row,col)
            if _p[row][col] == "#":
                if row == r and col == c:
                    pass
                else:
                    ct +=1
    if ct > 3:
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
    print(_p)
    _a = np.array(_p)
    count = -1
    #print("test")
    #print("\n".join(gen(_p)))
    while count == -1:
        print("new gen")
        n = deep_copy(gen(_p))
        count = check(_p, n)
        _p = deep_copy(n)
        print(count)
        print("\n".join(_p))
        #input()
    print("\n".join(n))
    print(count)
    