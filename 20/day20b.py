_t = {}
_sides = {}
_set = set()
with open("test.txt") as f:
    contents = f.read()
_s = contents.split("\n\n")

def _top(array):
    return array[0]

def _bot(array):
    return array[-1]

def _right(array):
    return [x[-1] for x in array]

def _left(array):
    return [x[0] for x in array]

def fliph(array):
    return [x[::-1] for x in array]

def flipv(array):
    return array[::-1]

def rotater(array):
    return [list(x) for x in zip(*array[::-1])]

def aprint(array):
    print()
    for row in array:
        print("".join(row))

def add_to_set(_t1,_t2):
    if _t1 > _t2:
        _set.add((_t1,_t2))
    else:
        _set.add((_t2,_t1))

sides=[_top,_bot,_right,_left]

def check_all_sides(_t1,_t2,arr1,arr2):
    for func in sides:
        for func2 in sides:
            if "".join(func(arr1)) == "".join(func2(arr2)):
                add_to_set(_t1,_t2)

def which_sides_match(arr1,arr2):
    for func in sides:
        for func2 in sides:
            if "".join(func(arr1)) == "".join(func2(arr2)):
                return(func.__name__,str(func2.__name__))

for tile in _s:
    #print(tile)
    _s2 = tile.split("\n")
    name = ""
    for _t2 in _s2:
        if "Tile" in _t2:
            name = int(_t2.strip().split()[1][0:-1])
        if name not in _t:
                _t[name] =[]
        else:
            _t[name].append(list(_t2))

for x in _t.keys():
    _sides[x] = 0

for key,v in _t.items():
    for key2,v2 in _t.items():
        if key != key2:
            temp = v2.copy()
            for x in range(3):
                check_all_sides(key,key2,v.copy(),temp.copy())
                temp = rotater(temp)
            #back to vertical
            temp = rotater(temp)
            temp = fliph(temp)
            check_all_sides(key,key2,v.copy(),temp.copy())
            temp = flipv(temp)
            check_all_sides(key,key2,v.copy(),temp.copy())

for x in _set:
    _sides[x[0]]+=1
    _sides[x[1]]+=1
total = 1
_l  = int(len(_t)**.5)

_big_picture = []
_bp_num = []
for number in range(_l):
    _big_picture.append([])
    _bp_num.append([])
    for number2 in range(_l):
        _big_picture[number].append([])
        _bp_num[number].append([])

print(_big_picture)
#build a picture  

start_corner = 0
for k,v in _sides.items():
    if v == 2:
        #print(k,v)
        start_corner = k
lrtiles = []
for item in _set:
    if start_corner in item:
        if item[0] == start_corner:
            lrtiles.append(item[1])
        else:
            lrtiles.append(item[0])
        
print(lrtiles)
print(start_corner)

#start trying to orient the start corner
stemp = _t[start_corner].copy()
temp = _t[lrtiles[0]].copy()
for y in range(3):
    _w = which_sides_match(stemp,temp)
    if _w != None:
        break
    temp = rotater(temp)
if _w == None:
    temp = fliph(temp)
    _w = which_sides_match(stemp,temp)
if _w == None:
    temp = flipv(temp)
    _w = which_sides_match(stemp,temp)
    
if _w[0] == '_left':
    stemp =fliph(stemp)
elif _w[0] == '_bot':
    stemp = fliph(rotater(stemp))
elif _w[0] == '_top':
    stemp = fliph(rotater(stemp))

if _w[1] == '_right':
    temp = fliph(temp)
elif _w[1] == '_bot':
    temp = rotater(temp)
elif _w[1] == '_top':
    temp = fliph(rotater(temp))
    #aprint(stemp)
    #aprint(temp)

_big_picture[0][0] = stemp.copy()
_big_picture[0][1] = temp.copy()
_bp_num[0][0] = start_corner
_bp_num[0][1] = lrtiles[0]

for line,row in enumerate(_big_picture):
    #print(line,row)
    for column, tile in enumerate(row):
        print(column)
        aprint(tile)

print(_bp_num)
