_t = {}
_sides = {}
_set = set()
with open("input.txt") as f:
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


def add_to_set(_t1,_t2):
    if _t1 > _t2:
        _set.add((_t1,_t2))
    else:
        _set.add((_t2,_t1))


def check_all_sides(_t1,_t2,arr1,arr2):
    if "".join(_top(arr1)) == "".join(_top(arr2)):
        add_to_set(key,key2)
    if "".join(_top(arr1)) == "".join(_right(arr2)):
        add_to_set(key,key2)
    if "".join(_top(arr1)) == "".join(_left(arr2)):
        add_to_set(key,key2)
    if "".join(_top(arr1)) == "".join(_bot(arr2)):
        add_to_set(key,key2)
    if "".join(_right(arr1)) == "".join(_right(arr2)):
        add_to_set(key,key2)
    if "".join(_right(arr1)) == "".join(_left(arr2)):
        add_to_set(key,key2)
    if "".join(_right(arr1)) == "".join(_bot(arr2)):
        add_to_set(key,key2)
    if "".join(_right(arr1)) == "".join(_top(arr2)):
        add_to_set(key,key2)
    if "".join(_left(arr1)) == "".join(_left(arr2)):
        add_to_set(key,key2)
    if "".join(_left(arr1)) == "".join(_right(arr2)):
        add_to_set(key,key2)
    if "".join(_left(arr1)) == "".join(_bot(arr2)):
        add_to_set(key,key2)
    if "".join(_bot(arr1)) == "".join(_bot(arr2)):
        add_to_set(key,key2)
    if "".join(_bot(arr1)) == "".join(_top(arr2)):
        add_to_set(key,key2)
    if "".join(_bot(arr1)) == "".join(_right(arr2)):
        add_to_set(key,key2)
    if "".join(_bot(arr1)) == "".join(_left(arr2)):
        add_to_set(key,key2)


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
        

#print(_t.keys())
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
for k,v in _sides.items():
    if v == 2:
        #print(k,v)
        total *=k
    
print(total)
