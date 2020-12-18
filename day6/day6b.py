with open("input.txt") as f:
    counter = 0
    _s = set()
    _a = []
    for line in f.readlines():
       _s = set()
       if len(line.strip()) == 0:
#            if len(_a) > 1:
#                _t = _a[0]
#                for thing in range(1,len(_a)):
#                    _t = _t.intersection(_a[thing])
#                counter = counter + len(_t)
#            else:
#                counter = counter + len(_a[0])
           counter = counter+(len(set.intersection(*_a)))
           _a = []
       else:
           for x in line.strip():
               _s.add(x)
           _a.append(_s)
#     _t = set()
#     if len(_a) > 1:
#         _t = _a[0]
#         for thing in range(1,len(_a)):
#             _t = _t.intersection(_a[thing])
#         counter = counter + len(_t)
#     else:
#         counter = counter + len(_a[0])
    counter = counter+(len(set.intersection(*_a)))
    print(counter)