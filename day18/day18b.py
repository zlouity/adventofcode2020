import math
def solver(_a):
    _ret = 1
    while "+" in _a:
        idx = _a.index("+")
        tot = int(_a[idx-1]) + int(_a[idx+1])
        _a.pop(idx-1)
        _a.pop(idx-1)
        _a.pop(idx-1)
        _a.insert(idx-1,tot)
    
    for thing in _a:
        if thing != "*":
            _ret *= int(thing)
    return(_ret)


with open("input.txt") as f:    
    _ex = [list(x.strip().replace(" ","")) for x in f.readlines()]
    #print(_ex)
    tot = 0
    for y in _ex:
        _s = False
        tok = 0
        ltot = 0
        q = []
        stack = []
        while tok  < len(y):
            if y[tok].isnumeric():
                if _s:
                    stack.append(y[tok])
                else:
                #print("Number",y[tok])
                    q.append(y[tok])
            elif y[tok] == "*":
                #print("Mult", y[tok])
                if y[tok+1].isnumeric():
                    if _s:
                        stack.append(y[tok])
                        stack.append(y[tok+1])
                    else:
                        q.append(y[tok])
                        q.append(y[tok+1])
                    tok +=1
                else:
                    if _s:
                        stack.append(y[tok])
                    else:
                        q.append(y[tok])
                        
            elif y[tok] == "+":
                #print("plus", y[tok])
                if y[tok+1].isnumeric():
                    if _s:
                        stack.append(y[tok])
                        stack.append(y[tok+1])
                    else:
                        q.append(y[tok])
                        q.append(y[tok+1])
                    tok +=1
                else:
                    if _s:
                        stack.append(y[tok])
                    else:
                        q.append(y[tok])
            elif y[tok] == "(":
                #print("lpar",y[tok])
                stack.append(y[tok])
                _s = True
            elif y[tok] == ")":
                #print("rpar",y[tok])
                #roll back to previous paren
                eq = []
                pop = stack.pop()
                while pop != "(":
                    eq.append(pop)
                    pop = stack.pop()
                eq.reverse()
                if len(stack) == 0:
                    q.append(solver(eq))
                    _s = False
                else:
                    stack.append(solver(eq))
            tok += 1
        tot += solver(q)
        #print(solver(q))

    print(tot)