from collections import defaultdict
with open('day22.txt') as f:
    o_p1_d  = [int(x.strip()) for x in f.readlines()]

with open('day22b.txt') as f:
    o_p2_d = [int(x.strip()) for x in f.readlines()]

_rounds = {}
counter = 0
def _new_game(_d1,_d2,game):
    #print("New Game", _d1,_d2)
    while len(_d1) > 0 and len(_d2) > 0:
        if _round(_d1,_d2,game):
            _rounds.pop(game)
            return True
    _rounds.pop(game)
    if len(_d1) >0:
        return True
    return False
    

def _round(_p1_d,_p2_d,game):
    global counter
    if game not in _rounds:
        _rounds[game] = defaultdict(list)
    if tuple(_p1_d) in _rounds[game][1] or tuple(_p2_d) in _rounds[game][2]:
        #print("true")
        counter+=1
        return True
    else:
        _rounds[game][1].append((tuple(_p1_d.copy())))
        _rounds[game][2].append((tuple(_p2_d.copy())))
    #print("Game "+str(game))
    #print("Player 1's deck: " + ",".join([str(x) for x in _p1_d]))
    #print("Player 2's deck: " + ",".join([str(x) for x in _p2_d]))
    t1 = _p1_d.pop(0)
    t2 = _p2_d.pop(0)
    #print("Player 1 plays: "+str(t1))
    #print("Player 2 plays: "+str(t2))
    result = None
    if t1 <= len(_p1_d) and t2 <= len(_p2_d):
        #input()
        result = _new_game(_p1_d[0:t1].copy(),_p2_d[0:t2].copy(),game+1)
        #print(result)
        if result:
            _p1_d.append(t1)
            _p1_d.append(t2)
        else:
           _p2_d.append(t2)
           _p2_d.append(t1) 
    else:
        if t1 > t2:
            _p1_d.append(t1)
            _p1_d.append(t2)
        else:
            _p2_d.append(t2)
            _p2_d.append(t1)
    #input()

_p1_win = False
while len(o_p1_d) > 0 and len(o_p2_d) > 0:
    if _round(o_p1_d,o_p2_d,1):
        _p1_win == True
        break
    #print(o_p1_d,o_p2_d)
    
print(o_p1_d)
print(o_p2_d)

score = 0
if len(o_p1_d) >0 or _p1_win:
    for x,v in enumerate(o_p1_d[::-1]):
        score+=(x+1)*v
else:
    for x,v in enumerate(o_p2_d[::-1]):
        score+=(x+1)*v

print(score)
print(counter)