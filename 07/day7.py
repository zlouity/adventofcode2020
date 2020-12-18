with open("input.txt") as f:
    _d = {}
    for line in f.readlines():
        _b = []
        _y = line.strip().split("bags contain")
        for x in _y[1].split(","):
            _b.append(x.strip().split()[1]+" "+x.strip().split()[2])
        _d[_y[0].strip()]= _b
    print(_d)
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
    print(_total_list)
    print(sum([1 for x in _total_list if "shiny gold" in x]))