# my ticket
#_mt = [79,193,53,97,137,179,131,73,191,139,197,181,67,71,211,199,167,61,59,127]
# de freitas ticket
_mt = [191,89,73,139,71,103,109,53,97,179,59,67,79,101,113,157,61,107,181,137]
_f = {}
_c = ""
with open('ticket_fields2.txt') as f:
    _c = [x.strip() for x in f.readlines()]
    for t in _c:
        f2 = t.split(":")
        r = f2[1].split(" or ")
        _f[f2[0]] = [(int(r[0].split("-")[0]),int(r[0].split("-")[1])),
                     (int(r[1].split("-")[0]),int(r[1].split("-")[1]))]
    
    #print(_f)
bad_tickets = []
with open('file16.txt') as f3:
    _n = [x.strip() for x in f3.readlines()]
    for v,t in enumerate(_n):
        for x in t.split(","):
            iv = 0
            for k in _f:
                if (_f[k][0][0] <= int(x) <= _f[k][0][1]) or (_f[k][1][0] <= int(x) <= _f[k][1][1]):
                    iv +=1
                    break
            if iv==0:
                bad_tickets.append(v)
                break
            
good_tickets = [x.split(',') for v,x in enumerate(_n) if v not in bad_tickets]
poss = {}
for x in _f:
    poss[x] = []
print(poss)
print(good_tickets)
_l = len(good_tickets[0])
for cat in poss:
    #check each column in each ticket and if its a possiblity
    for col in range(_l):
        iv = 0
        for tkt in good_tickets:
            if (_f[cat][0][0] <= int(tkt[col]) <= _f[cat][0][1]) or (_f[cat][1][0] <= int(tkt[col]) <= _f[cat][1][1]):
                pass
            else:
                iv +=1
                break
        
        if iv==0:
            poss[cat].append(col)
            
used = set()
final = {}
for v in sorted(poss, key=lambda k:len(poss[k])):
    print(v,poss[v])
    if len(poss[v]) == 1:
        final[v] = poss[v][0]
        used = used.union(poss[v])
    else:
        final[v] = list(set(poss[v]).difference(used))[0]
        used = used.union([final[v]])
    
print(final)
total = 1
for k,x in final.items():
    if "departure" in k:
        total*=_mt[x]
print(total)