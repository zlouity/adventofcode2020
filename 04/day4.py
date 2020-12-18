with open("input.txt") as f:
    counter =0
    passports = []
    _d={}
    for line in f.readlines():
        _t = line.strip()
        if _t =="":
            print("new")
            passports.append(_d)
            _d = {}
        else:
            for x in _t.split(" "):
                _c = x.split(":")
                _d[_c[0]]=_c[1]
    passports.append(_d)
    
    
    for thing in passports:
#         print(thing)
        if len(thing)==7 and 'cid' not in thing:
            counter +=1    
        if len(thing) == 8:
            counter+=1
    print(counter)
            
        