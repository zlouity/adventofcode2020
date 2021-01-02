import re
import copy
_t = {}
_sides = {}
_set = set()

monster_re = re.compile("(?=(#....##....##....###))")
monster_re2 = re.compile(".#(..#){5}...")
relative_sea_monster_positions = [(-1, 18), (0, 0), (0, 5), (0, 6), (0, 11),
                                  (0, 12), (0, 17), (0, 18), (0, 19), (1, 1),
                                  (1, 4), (1, 7), (1, 10), (1, 13), (1, 16)]

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

def aprint(array):
    print()
    for trow in array:
        print("".join(trow))

def add_to_set(_t1, _t2):
    if _t1 > _t2:
        _set.add((_t1, _t2))
    else:
        _set.add((_t2, _t1))

sides = [_top, _bot, _right, _left]

def check_all_sides(_t1, _t2, arr1, arr2):
    for func in sides:
        for func2 in sides:
            if "".join(func(arr1)) == "".join(func2(arr2)):
                add_to_set(_t1, _t2)

def which_sides_match(arr1, arr2):
    for func in sides:
        for func2 in sides:
            if "".join(func(arr1)) == "".join(func2(arr2)):
                return(func.__name__, str(func2.__name__))
    return None

def find_monsters(arr):
    counter = set()
    for idx, idx_item in enumerate(arr):
        matches = monster_re.findall("".join(idx_item))
        for match in matches:
            sidx = "".join(idx_item).index(match)
            if arr[idx-1][sidx+18] == "#" and \
                    monster_re2.findall("".join(arr[idx+1][sidx:sidx+20])):
                counter.add((idx, sidx))
    return counter
#tile prep splitting off numbers and tiles
for tile in _s:
    #print(tile)
    _s2 = tile.split("\n")
    name = ""
    for _t2 in _s2:
        if "Tile" in _t2:
            name = int(_t2.strip().split()[1][0:-1])
        if name not in _t:
            _t[name] = []
        else:
            _t[name].append(list(_t2))
#initialize the dictionary
for x in _t:
    _sides[x] = 0
#finding the sides that match other sides
for key, v in _t.items():
    for key2, v2 in _t.items():
        if key != key2:
            temp = copy.deepcopy(v2)
            for x in range(4):
                check_all_sides(key, key2, copy.deepcopy(v), copy.deepcopy(temp))
                temp = rotater(temp)
            #back to vertical
            check_all_sides(key, key2, copy.deepcopy(v), copy.deepcopy(fliph(temp)))
            check_all_sides(key, key2, copy.deepcopy(v), copy.deepcopy(flipv(temp)))
#count the number of matching sides for each tile
for x in _set:
    _sides[x[0]] += 1
    _sides[x[1]] += 1
#picture is square, calculate the number of tiles in a side
_l = int(len(_t)**.5)
#make arrays to hold the big picture and an array to hold the tile numbers
_big_picture = []
_bp_num = []
for number in range(_l):
    _big_picture.append([])
    _bp_num.append([])
    for number2 in range(_l):
        _big_picture[number].append([])
        _bp_num[number].append(0)
#build a picture
start_corner = 0
for k, v in _sides.items():
    if v == 2:
        start_corner = k
lrtiles = []
#find the initial corner tiles
for item in _set:
    if start_corner in item:
        if item[0] == start_corner:
            lrtiles.append(item[1])
        else:
            lrtiles.append(item[0])
#orient the start corner so the right and bottom sides are facing in the correct direction
stemp = copy.deepcopy(_t[start_corner])
temp = copy.deepcopy(_t[lrtiles[0]])
temp2 = copy.deepcopy(_t[lrtiles[1]])
#orient the right side of the start tile
for y in range(3):
    _w = which_sides_match(stemp, temp)
    if _w is not None:
        break
    temp = rotater(temp)
if _w is None:
    temp = fliph(temp)
    _w = which_sides_match(stemp, temp)
if _w is None:
    temp = flipv(temp)
    _w = which_sides_match(stemp, temp)
if _w[0] == '_left':
    stemp = fliph(stemp)
elif _w[0] == '_bot':
    stemp = fliph(rotater(stemp))
elif _w[0] == '_top':
    stemp = fliph(rotater(stemp))
#orient start tile top and bottom
for y in range(3):
    _v = which_sides_match(stemp, temp2)
    if _v is not None:
        break
    temp2 = rotater(temp2)
if _v is None:
    temp2 = fliph(temp2)
    _w = which_sides_match(stemp, temp2)
if _v is None:
    temp2 = flipv(temp2)
    _v = which_sides_match(stemp, temp2)
#only possible switch is if second match is on top and needs to be flipped vertically
if _v[0] == "_top":
    stemp = flipv(stemp)
#append the first tile and tile number
_big_picture[0][0] = copy.deepcopy(stemp)
_bp_num[0][0] = start_corner
#keep track of which tiles have been placed
used_nums = set()
used_nums.add(start_corner)
#solve the first row by matching the right sides from left to right
for x, v in enumerate(_big_picture[0]):
    if not v:
        possible_tiles = []
        for z in _set:
            if _bp_num[0][x-1] in z:
                if z[0] == _bp_num[0][x-1]:
                    possible_tiles.append(z[1])
                else:
                    possible_tiles.append(z[0])
        possible_tiles = set(possible_tiles).difference(used_nums)
        for tile in possible_tiles:
            search = False
            temp = copy.deepcopy(_t[tile])
            for y in range(4):
                _w = which_sides_match(_big_picture[0][x-1], temp)
                if _w == ('_right', '_left'):
                    search = True
                    break
                temp = copy.deepcopy(fliph(temp))
                _w = which_sides_match(_big_picture[0][x-1], temp)
                if _w == ('_right', '_left'):
                    search = True
                    break
                temp = copy.deepcopy(flipv(temp))
                _w = which_sides_match(_big_picture[0][x-1], temp)
                if _w == ('_right', '_left'):
                    search = True
                    break
                temp = copy.deepcopy(fliph(flipv(temp)))
                temp = rotater(temp)
            if search:
                break
        _bp_num[0][x] = tile
        _big_picture[0][x] = copy.deepcopy(temp)
        used_nums.add(tile)
#rotate and add all remaining rows
#match the bottom of the previous row to the top of the current possible tile
for line_num in range(1, len(_big_picture)):
    for num, item in enumerate(_big_picture[line_num]):
        if not item:
            possible_tiles = []
            for z in _set:
                if _bp_num[line_num-1][num] in z:
                    if z[0] == _bp_num[line_num-1][num]:
                        possible_tiles.append(z[1])
                    else:
                        possible_tiles.append(z[0])
            possible_tiles = set(possible_tiles).difference(used_nums)
            for tile in possible_tiles:
                temp = copy.deepcopy(_t[tile])
                search = False
                for y in range(4):
                    _w = which_sides_match(_big_picture[line_num-1][num], temp)
                    if _w == ('_bot', '_top'):
                        search = True
                        break
                    temp = copy.deepcopy(fliph(temp))
                    _w = which_sides_match(_big_picture[line_num-1][num], temp)
                    if _w == ('_bot', '_top'):
                        search = True
                        break
                    temp = copy.deepcopy(flipv(temp))
                    _w = which_sides_match(_big_picture[line_num-1][num], temp)
                    if _w == ('_bot', '_top'):
                        search = True
                        break
                    temp = copy.deepcopy(fliph(flipv(temp)))
                    temp = rotater(temp)
                if search:
                    break
            _bp_num[line_num][num] = tile
            _big_picture[line_num][num] = copy.deepcopy(temp)
            used_nums.add(tile)
#strip the outer edge of each of the tiles and
for line, row in enumerate(_big_picture):
    #print(line,row)
    for column, tile in enumerate(row):
        #print(_bp_num[line][column])
        #aprint(tile)
        #aprint([x[1:-1] for x in tile[1:-1]])
        _big_picture[line][column] = [x[1:-1] for x in tile[1:-1]]
#array to hold the entire stitched together picture
total_picture = []
#join all of the rows in all of the tiles together
for line, row in enumerate(_big_picture):
    for z in range(len(row[0])):
        line = ""
        for column in row:
            line = line+"".join(column[z])
        total_picture.append(list(line))
#sea monster image
#go through all possible flips to find the correct
#orientation for the picture
for y in range(4):
    found_monsters = find_monsters(total_picture)
    if found_monsters:
        break
    total_picture = fliph(total_picture)
    found_monsters = find_monsters(total_picture)
    if found_monsters:
        break
    total_picture = flipv(total_picture)
    found_monsters = find_monsters(total_picture)
    if found_monsters:
        break
    total_picture = fliph(flipv(total_picture))
    total_picture = rotater(total_picture)
#hightlight all the sea monsters
for s_pt in found_monsters:
    for mon_pt in relative_sea_monster_positions:
        if total_picture[s_pt[0]+mon_pt[0]][s_pt[1]+mon_pt[1]] == "#":
            total_picture[s_pt[0]+mon_pt[0]][s_pt[1]+mon_pt[1]] = "O"
#pretty printing the picture
aprint(total_picture)
count = 0
for x in total_picture:
    count += x.count("#")
print("Found {} Sea Monsters!".format(len(found_monsters)))
print("The sea has a roughness factor of {}".format(count))
