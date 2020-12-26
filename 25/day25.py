#test_cn = 5764801
#test_dn = 17807724
# card_num = 5764801
# door_num = 17807724

card_num = 15335876
door_num = 15086442

temp_num = 1
card_loop_size =0
while temp_num != card_num:
    temp_num = (temp_num*7)%20201227
    card_loop_size+=1

print(card_loop_size)

temp_num = 1
door_loop_size =0
while temp_num != door_num:
    temp_num = (temp_num*7)%20201227
    door_loop_size+=1

print(door_loop_size)

temp_num = 1
for x in range(card_loop_size):
    temp_num = (temp_num*door_num)%20201227

print(temp_num)