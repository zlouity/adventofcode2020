import re
import copy
_t = {}
_sides = {}
_set = set()

monster_re = re.compile("#....##....##....###")
monster_re2 = re.compile(".#(..#){5}...")

with open("day20.txt") as f:
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
            
def find_monsters(arr):
#     print("Finding Monsters")
    counter = 0
    #aprint(arr)
    for v,x in enumerate(arr):
        matches = monster_re.findall("".join(x))
#         if len(matches) > 0:
#             aprint(arr)
        for match in matches:
#             print(v,match,"".join(x).index(match))
            sidx = "".join(x).index(match)
#             print(arr[v-1][sidx+18])
            if arr[v-1][sidx+18] == "#" and len(monster_re2.findall("".join(arr[v+1][sidx:sidx+20]))) > 0:
                counter+=1
    return counter

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
            temp = copy.deepcopy(v2)
            for x in range(4):
                check_all_sides(key,key2,copy.deepcopy(v),copy.deepcopy(temp))
                temp = rotater(temp)
            #back to vertical
            check_all_sides(key,key2,copy.deepcopy(v),copy.deepcopy(fliph(temp)))
            check_all_sides(key,key2,copy.deepcopy(v),copy.deepcopy(flipv(temp)))

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

# print(_big_picture)
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
stemp = copy.deepcopy(_t[start_corner])
temp = copy.deepcopy(_t[lrtiles[0]])
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

_big_picture[0][0] = copy.deepcopy(stemp)
_big_picture[0][1] = copy.deepcopy(temp)
_bp_num[0][0] = start_corner
_bp_num[0][1] = lrtiles[0]

used_nums = set()
used_nums.add(start_corner)
used_nums.add(lrtiles[0])
#solve the first row
#print("solve for the first row")
for x,v in enumerate(_big_picture[0]):
    if len(v) == 0:
        possible_tiles = []
        for z in _set:
            if _bp_num[0][x-1] in z:
                if z[0] == _bp_num[0][x-1]:
                    possible_tiles.append(z[1])
                else:
                    possible_tiles.append(z[0])
        
        possible_tiles = set(possible_tiles).difference(used_nums)
        #print("possible tiles")
        #print(possible_tiles)
        if 1063 in possible_tiles:
            pass
        for item in possible_tiles:
            search = False
            temp = copy.deepcopy(_t[item])
            for y in range(4):
                _w = which_sides_match(_big_picture[0][x-1],temp)
                if _w == ('_right','_left'):
                    search = True
                    break
                temp = rotater(temp)
            if search:
                break
            if _w !=  ('_right','_left'):
                temp = copy.deepcopy(fliph(temp))
                _w = which_sides_match(_big_picture[0][x-1],temp)
            if _w != ('_right','_left'):
                temp = copy.deepcopy(flipv(fliph(temp)))
                _w = which_sides_match(_big_picture[0][x-1],temp)
            if _w != ('_right','_left'):
                temp = copy.deepcopy(fliph(temp))
                _w = which_sides_match(_big_picture[0][x-1],temp)
            
            if _w == ('_right','_left'):
                break
        
        #aprint(temp)
        _bp_num[0][x] = item
        _big_picture[0][x] = copy.deepcopy(temp)
        used_nums.add(item)
                


print(_bp_num)
print(_big_picture)
#fix all remaining rows
#print("solve remaining rows")
for line_num in range(1,len(_big_picture)):
    for num,item in enumerate(_big_picture[line_num]):
        if len(item) == 0:
            possible_tiles = []
            for z in _set:
                if _bp_num[line_num-1][num] in z:
                    if z[0] == _bp_num[line_num-1][num]:
                        possible_tiles.append(z[1])
                    else:
                        possible_tiles.append(z[0])
            print(possible_tiles)
            possible_tiles = set(possible_tiles).difference(used_nums)
            print("possible tiles")
            print(possible_tiles)
            for item in possible_tiles:
                temp = copy.deepcopy(_t[item])
                search = False
                for y in range(4):
                    _w = which_sides_match(_big_picture[line_num-1][num],temp)
                    if _w == ('_bot','_top'):
                        search = True
                        break
                    temp = rotater(temp)
                if search:
                    break    
                if _w !=  ('_bot','_top'):
                    temp = copy.deepcopy(fliph(temp))
                    _w = which_sides_match(_big_picture[line_num-1][num],temp)
                if _w != ('_bot','_top'):
                    temp = copy.deepcopy(flipv(fliph(temp)))
                    _w = which_sides_match(_big_picture[line_num-1][num],flipv(temp))
                if _w != ('_right','_left'):
                    temp = copy.deepcopy(fliph(temp))
                    _w = which_sides_match(_big_picture[line_num-1][num],temp)
                
                if _w == ('_bot','_top'):
                    break
            #print(item)
            #print(type(item))
            #print(item)
            #aprint(temp)
            _bp_num[line_num][num] = item
            _big_picture[line_num][num] = copy.deepcopy(temp)
            used_nums.add(item)


print(_bp_num)
#print("print the big picture")
for line,row in enumerate(_big_picture):
    #print(line,row)
    for column, tile in enumerate(row):
        #print(_bp_num[line][column])
        #aprint(tile)
        #aprint([x[1:-1] for x in tile[1:-1]])
        _big_picture[line][column] = [x[1:-1] for x in tile[1:-1]]
        


total_picture = []
for line,row in enumerate(_big_picture):
    for z in range(len(row[0])):
        line = ""
        for column in row:
            line = line+"".join(column[z])
        total_picture.append(list(line))

#sea monster image
#aprint(rotater(rotater(rotater(total_picture))))
#test image
#aprint(fliph(total_picture))
temp =copy.deepcopy(total_picture)
found_monsters = 0
for y in range(4):
    found_monsters = find_monsters(temp)
    if found_monsters > 0:
        break
    temp = rotater(temp)
if found_monsters == 0:
    temp = fliph(temp)
    found_monsters = find_monsters(temp)
if found_monsters == 0:
    temp = flipv(temp)
    found_monsters = find_monsters(temp)


count = 0
for x in total_picture:
    count += x.count("#")

#print(count)
print(found_monsters)
print(count)


