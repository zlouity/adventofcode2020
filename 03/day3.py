with open("input.txt") as f:
    array = []
    pos = (0,0)
    x = 3
    y =1
    for line in f.readlines():
        array.append(line.strip())
        
    counter = 0
    while y < len(array):
        if array[y][x] =="#":
            counter +=1
        x = x+3
        x = x%len(array[y])
        y=y+1
        
print(counter)   