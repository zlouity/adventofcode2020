class node:
    
    def __init__(self, _next = None):
        self.next = _next
    

nodes = {}


def main(q):
    #start = time.time()
    #_test = [3,8,9,1,2,5,4,6,7]
    _test = [6,5,3,4,2,7,9,1,8]
    for x in range(10,1000001):
        _test.append(x)
    pickup = [0,0,0]
    temp = None
    for j in _test[::-1]:
        nodes[j] = node(temp)
        temp = nodes[j]
    nodes[_test[-1]].next = nodes[_test[0]]
    reverse_nodes = {v:k for k,v in nodes.items()}
    #print(_test)
    idx = _test[0]
    _l = len(_test)
    for y in range(q):
        #print("cups",_test)
        _cc = nodes[idx]
        #print("current cup", reverse_nodes[_cc])
        temp = _cc.next
        for x in range(3):
            pickup[x] = reverse_nodes[temp]
            temp = temp.next
        _cc.next = temp
        #print("pickup",pickup)
        dest_cup = None
        possible_idx = idx-1
        while dest_cup == None:
            if possible_idx in pickup:
                possible_idx -=1
            elif possible_idx == 0:
                possible_idx = max(_test)
            else:
                dest_cup = possible_idx
        ins = nodes[dest_cup]
        ins_next = ins.next
        for z in pickup:
            ins.next = nodes[z]
            ins = nodes[z]
            
        ins.next = ins_next
        idx = reverse_nodes[_cc.next]

    curr = nodes[1].next
    num1 = reverse_nodes[curr]
    num2 = reverse_nodes[curr.next]
    print(num1,num2)
    print(num1*num2)
    
    #_s = ""
    #while reverse_nodes[curr] != 1:
    #    _s += str(reverse_nodes[curr])
    #    curr = curr.next
    #print(_s)
    
main(10000000)