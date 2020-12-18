def check_slide(_l,num):
    x = 0
    while x+num < len(_l):
        if sum(_l[x:x+num]) == 25918798:
            print(_l[x],_l[x+num-1])
            print(min(_l[x:x+num-1])+max(_l[x:x+num-1]))
            return True
        x+=1
    return False
with open("input.txt") as f:
    _p = []
    for line in f.readlines():
        _p.append(int(line.strip()))
    for t in range(2,len(_p)):
        if check_slide(_p,t):
            break