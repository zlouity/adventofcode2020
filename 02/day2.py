with open("input.txt") as f:
    counter = 0
    for line in f.readlines():
        banana =line.strip().split(":")
        password = banana[-1]
        items= banana[0].split(" ")
#         print(items)
        letter = items[-1]
        num1 = int(items[0].split("-")[0])
        num2 = int(items[0].split("-")[1])
        #print(password,items,letter,num1,num2)
        if num1<=password.count(letter)<=num2:
            counter+=1
    print(counter)