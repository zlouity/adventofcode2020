with open("input.txt") as f:
    highest = 0
    for line in f.readlines():
       s =line.strip()[0:7]
       r =line.strip()[7:10]
       s = s.replace("F","0").replace("B","1")
       r = r.replace("R","1").replace("L","0")
       s = int(s,2)
       r = int(r,2)
       #print((s * 8 + r))
       if (s*8+r) > highest:
           highest = (s*8+r)
print(highest)
       