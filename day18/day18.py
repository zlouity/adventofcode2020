
def solver(_a):
    _ret = int(_a[0])
    x = 1
    while x < len(_a)-1:
        if _a[x] == "*":
            _ret = _ret*int(_a[x+1])
        else:
            _ret = _ret+int(_a[x+1])
        x = x+2
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

    print(tot)