import time
start = time.time()
with open("input.txt") as f:
    _ex = [x.strip() for x in f.readlines()]
    
_tiles = {}

def check_gen(_p):
    counter = 0
    #w
    if (_p[0]-2,_p[1]) in _tiles:
        if _tiles[(_p[0]-2,_p[1])] == 'b':
            counter += 1
    #e
    if (_p[0]+2,_p[1]) in _tiles:
        if _tiles[(_p[0]+2,_p[1])] == 'b':
            counter += 1
    #se
    if (_p[0]+1,_p[1]-1) in _tiles:
        if _tiles[(_p[0]+1,_p[1]-1)] == 'b':
            counter += 1
    #sw
    if (_p[0]-1,_p[1]-1) in _tiles:
        if _tiles[(_p[0]-1,_p[1]-1)] == 'b':
            counter += 1
    #nw
    if (_p[0]-1,_p[1]+1) in _tiles:
        if _tiles[(_p[0]-1,_p[1]+1)] == 'b':
            counter += 1
    #ne
    if (_p[0]+1,_p[1]+1) in _tiles:
        if _tiles[(_p[0]+1,_p[1]+1)] == 'b':
            counter += 1
    if counter == 2:
        return True
    return False

def check_flip(_p):
    counter = 0
    #w
    if (_p[0]-2,_p[1]) in _tiles:
        if _tiles[(_p[0]-2,_p[1])] == 'b':
            counter += 1
    #e
    if (_p[0]+2,_p[1]) in _tiles:
        if _tiles[(_p[0]+2,_p[1])] == 'b':
            counter += 1
    #se
    if (_p[0]+1,_p[1]-1) in _tiles:
        if _tiles[(_p[0]+1,_p[1]-1)] == 'b':
            counter += 1
    #sw
    if (_p[0]-1,_p[1]-1) in _tiles:
        if _tiles[(_p[0]-1,_p[1]-1)] == 'b':
            counter += 1
    #nw
    if (_p[0]-1,_p[1]+1) in _tiles:
        if _tiles[(_p[0]-1,_p[1]+1)] == 'b':
            counter += 1
    #ne
    if (_p[0]+1,_p[1]+1) in _tiles:
        if _tiles[(_p[0]+1,_p[1]+1)] == 'b':
            counter += 1
    if counter > 2 or counter == 0:
        return False
    return True

def _round(_pop):
    _ret = {}
    for item in _pop:
        if item in _tiles:
            if _tiles[item] == 'b':
                if check_flip(item):
                    _ret[item] = 'b'
            else:
                if check_gen(item):
                    _ret[item] = 'b'
        else:
            if check_gen(item):
                _ret[item] = 'b'
    return _ret



def possn(_a):
    #include all of the b tiles
    _ret = set(_a)
    for x in _a:
        #w
        _ret.add((x[0]-2,x[1]))
        #e
        _ret.add((x[0]+2,x[1]))
        #se
        _ret.add((x[0]+1,x[1]-1))
        #sw
        _ret.add((x[0]-1,x[1]-1))
        #nw
        _ret.add((x[0]-1,x[1]+1))
        #ne
        _ret.add((x[0]+1,x[1]+1))
    return _ret


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
    #print(end)
    if end in _tiles:
        if _tiles[end] == 'b':
            _tiles[end] = 'w'
        else:
            _tiles[end] = 'b'
    else:
        _tiles[end] = 'b'

#print(_tiles)

for z in range(100):
    _p = possn(_tiles.keys())
    _tiles = _round(_p)
#print(_tiles)

print(sum([1 for k,v in _tiles.items() if v == 'b']))
print(time.time()-start)