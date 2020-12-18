with open("input.txt") as f:
    counter = 0
    for line in f.readlines():
        banana =line.strip().split(":")
        password = banana[-1].strip()
        items= banana[0].split(" ")
#         print(items)
        letter = items[-1]
        num1 = int(items[0].split("-")[0])
        num2 = int(items[0].split("-")[1])
        #print(num1-1,num2-1)
        if (password[num1-1]==letter) ^ (password[num2-1]==letter):
            counter+=1
#         if password[num1-1]==letter:
#             if password[num2-1]!=letter:
#                 counter+=1           
#         elif password[num2-1]==letter:
#             if password[num1-1]!=letter:
#                 counter+=1
                
    print(counter)