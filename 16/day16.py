
_mt = [79,193,53,97,137,179,131,73,191,139,197,181,67,71,211,199,167,61,59,127]
_f = {}
_c = ""
with open('ticket_fields.txt') as f:
    _c = [x.strip() for x in f.readlines()]
    for t in _c:
        f2 = t.split(":")
        r = f2[1].split(" or ")
        _f[f2[0]] = [(int(r[0].split("-")[0]),int(r[0].split("-")[1])),
                     (int(r[1].split("-")[0]),int(r[1].split("-")[1]))]
    
    print(_f)
counter  = 0

with open('input.txt') as f3:
    _n = [x.strip() for x in f3.readlines()]
    for t in _n:
        for x in t.split(","):
            iv = 0
            for k in _f:
                if (_f[k][0][0] <= int(x) <= _f[k][0][1]) or (_f[k][1][0] <= int(x) <= _f[k][1][1]):
                    iv +=1
                    break
            if iv==0:
                counter += int(x)
            

print(counter)
                    
            
                