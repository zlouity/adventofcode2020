import numpy as np



def check_gen(_a,active):
    counter =0
    for i in range(_a[0]-1,_a[0]+2):
        for j in range(_a[1]-1,_a[1]+2):
            for k in range(_a[2]-1,_a[2]+2):
                if (i,j,k) != _a and (i,j,k) in active:
                    counter +=1
    if counter == 3:
        return True
                    
    return False

def check_live(_a,active):
    counter = 0
    for i in range(_a[0]-1,_a[0]+2):
        for j in range(_a[1]-1,_a[1]+2):
            for k in range(_a[2]-1,_a[2]+2):
                if (i,j,k) != _a and (i,j,k) in active:
                    counter +=1
    if counter == 3 or counter == 2:
        return True
                    
    return False

def cycle(active,possN):
    new_act = []
    for point in possN:
        if point in active:
            if check_live(point,active):
                new_act.append(point)            
        else:
            if check_gen(point,active):
                new_act.append(point)
                        
    return new_act

def possN(_a):
    _ret = set()
    for x in _a:
        for i in range(x[0]-1,x[0]+2):
            for j in range(x[1]-1,x[1]+2):
                for k in range(x[2]-1,x[2]+2):
                    _ret.add((i,j,k))
    return _ret
                    


with open("input.txt") as f:    
    _ex = [list(x.strip()) for x in f.readlines()]
    active = []
    for x,v in enumerate(_ex):
        for y,w in enumerate(v):
            if w == "#":
                active.append((x,y,0))
                
    print(active)
    for x in range(6):
        active = cycle(active,possN(active))
    print(len(active))
    #print(cycle(active,possN(active)))
    #print(_ex)
#     for a,x in enumerate(_ex):
#         for b,y in enumerate(x):
#             _ex[a][b] = int(y)
#     
#     _ex = np.array(_ex)
#     _bx = np.zeros(_ex.shape,dtype=int)
#     _ax = np.zeros(_ex.shape,dtype=int)
#     stack = np.dstack((_bx,_ex,_ax))
#     stack = np.pad(stack,[(1,1),(1,1),(0,0)],mode='constant')
#     
#     for i in range(1,stack.shape[0]):
#         for j in range(1,stack.shape[1]):
#             for k in range(1,stack.shape[2]):
#                 if stack[i,j,k] == 1:
#                     a_print(stack[i-1:i+2,j-1:j+2,k-1:k+2])
#                     prod = kernel*stack[i-1:i+2,j-1:j+2,k-1:k+2]
#                     a_print(prod)
#                     print(np.count_non_zero(prod.count))
#                 elif stack[i,j,k] == 0:
#                     pass
# 
# def a_print(array):
#     print("printing array")
#     for i in range(array.shape[2]):
#         print(str(array[:,:,i])+"\n")


# kernel = np.ones(27,dtype=int).reshape(3,3,3)
# kernel[1,1,1]=0
# a_print(kernel)