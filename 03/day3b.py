with open("day3.txt") as f:
    array = []  
    for line in f.readlines():
        array.append(line.strip())
    
def tree_counter(_array):
    counter = 0
    x =_array[0]
    y =_array[1]
    while y < len(array):
        if array[y][x] =="#":
            counter+=1
        x = x+_array[0]
        x = x%len(array[y])
        y=y+_array[1]
        
    return counter
    
items=[[1,1],[3,1],[5,1],[7,1],[1,2]]
multiply = 1
for thing in items:
    multiply*=tree_counter(thing)
    #print(tree_counter(thing))
print(multiply)