
def count_bags(_d,_y,_z,_st):
    print(_z[_st])
    if "other bags" in _d[_st][0]:
        return 0
    else:
        _t = 0
        for i,v in _z[_st].items():
            _t+=(v+v*count_bags(_d,_y,_z,i))
        return _t


with open("input.txt") as f:
    _d = {}
    _q = {}
    _z = {}
    for line in f.readlines():
        _b = []
        _c = {}
        _y = line.strip().split("bags contain")
        total = 0
        for x in _y[1].split(","):
            
            _b.append(x.strip().split()[1]+" "+x.strip().split()[2])
            if "no" in x:
                _c[x.strip().split()[1]+" "+x.strip().split()[2]] = 0
                total += 0
            else:
                _c[x.strip().split()[1]+" "+x.strip().split()[2]] = int(x.strip().split()[0])
                total +=int(x.strip().split()[0])
        _d[_y[0].strip()]= _b
        _q[_y[0].strip()]= total
        _z[_y[0].strip()]= _c
    #print(_d)
    _total_list = []
    for t in _d:
        temp_list = []
        queue =_d[t].copy()
        while len(queue) > 0:
            current = queue.pop(0)
            if current in _d:
                temp_list.append(current)
                queue.extend(_d[current])
            else:
                temp_list.append(current)
        _total_list.append(temp_list)
    #print(_z)
    #print(_total_list)
    print(sum([1 for x in _total_list if "shiny gold" in x]))
    #print(_d['shiny gold'])
    queue = _z['shiny gold']
    #o = 0
    #print(queue)
    #for cur,val in queue.items():
#        o+=count_bags(_d,_q,_z,cur)
#     while len(queue) > 0:
#         current,value = queue.popitem()
#         if current in _z and _q[current]!=0:
#             o+=count_bags(_d,_q,_z,current)
#             #print(count_bags(_d,_q,current))
#             if _d[current][0] != "other bags.":
#                 queue.update(_z[current])
    print(count_bags(_d,_q,_z,'shiny gold'))