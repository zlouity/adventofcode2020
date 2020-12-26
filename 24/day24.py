with open("input.txt") as f:
    _ex = [x.strip() for x in f.readlines()]
    
_tiles = {}

for line in _ex:
    pt = [0,0]
    path = line
    while len(path) > 0:
        double = True
        if path[0] == 'w':
           pt[0] -=2
           double = False
        elif path[0] == 'e':
            pt[0] +=2
            double = False
        elif path[0:2] == 'se':
            pt[0] +=1
            pt[1] -=1
        elif path[0:2] == 'sw':
            pt[0] -=1
            pt[1] -=1
        elif path[0:2] == 'nw':
            pt[0] -=1
            pt[1] +=1
        elif path[0:2] == 'ne':
            pt[0] +=1
            pt[1] +=1
        if double:
            path = path[2:]
        else:
            path = path[1:]
        
    end = tuple(pt)
    print(end)
    if end in _tiles:
        if _tiles[end] == 'b':
            _tiles[end] = 'w'
        else:
            _tiles[end] = 'b'
    else:
        _tiles[end] = 'b'

print(_tiles)
print(sum([1 for k,v in _tiles.items() if v == 'b']))
    