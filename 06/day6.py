with open("input.txt") as f:
    counter = 0
    _s = set()
    for line in f.readlines():
       if len(line.strip()) == 0:
           counter = counter + len(_s)
           _s = set()
       else:
           for x in line.strip():
               _s.add(x)
    print(counter+len(_s))