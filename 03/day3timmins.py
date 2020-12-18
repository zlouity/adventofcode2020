file = open("input.txt")
contents = file.read()
contents = contents.split("\n")
count = 0
position = 1
row = 0
while row < len(contents):
    #print (contents[row],position%31)
    #print(row,position%31)
    x =  (contents[row][(position%31)-1])
    if x == "#":
        #print ("yup")
        count +=1
    position+=1
    row += 2
    
print (count)    
    
print(33*72*207*90*60)