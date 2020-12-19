import re
_g = {}

def _re(rule):
    _ret_re = ""
    #terminal character
    if type(_g[rule]) == str:
        return _g[rule]
    #single string of production
    elif type(_g[rule][0]) == int:
        for prod in _g[rule]:
            _ret_re = _ret_re+"("+ _re(prod) + ")"
    #multiple options
    else:
#         _ret_re = _ret_re + "("
        for prod_opts in _g[rule]:
            _ret_re = _ret_re + "("
            for prod in prod_opts:
                _ret_re = _ret_re+"("+ _re(prod) + ")"
            if prod_opts != _g[rule][-1]:
                _ret_re = _ret_re + ")|"
            else:
                _ret_re = _ret_re + ")"
    
    return _ret_re



with open("test2_grammar.txt") as f:    
    _ex = [x.strip() for x in f.readlines()]
    print(_ex)
    for x in _ex:
        rule = x.split(":")[0]
        prod = x.split(":")[1].strip()
        if "\"" in x:
            prod = prod.replace("\"","")
        elif "|" in x:
            prod = [[int(s) for s in prod.split("|")[0].strip().split()],
                    [int(s) for s in prod.split("|")[1].strip().split()]]
        else:
            prod = [int(s) for s in x.split(":")[1].strip().split()]
        
        _g[int(rule)]=prod
    print(_g)
    #print(_re(0))
    final_re = re.compile("^"+_re(0)+"$")
    #print(final_re.match("ababbb"))

counter = 0
with open("test2.txt") as g:
    for item in g.readlines():
        if final_re.match(item.strip()) != None:
           counter+=1
        
print(counter)
    
    

#     stack =[-1]
#     opt_stack = []
#     curr = 0
#     for prod in reversed(_g[_r]):
#         stack.append(prod)
#     print(stack)
#     while len(stack) > 0 and curr < len(_s):
#         i = stack.pop()
#         if i in _g and type(_g[i]) == list:
#             if len(_g[i]) > 1:
#                 rollback = stack.copy()
#                 opt_stack.extend(_g[i])
#             
#         elif i in _g and type(_g[i]) == str:
#             if i == _s[0]:
#                 curr+=1
#             elif len(opt_stack) > 0: