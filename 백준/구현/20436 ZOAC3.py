line_one = "qwertyuiop"
line_two = "asdfghjkl"
line_three = "zxcvbnm"

left_keys = "qwertasdfgzxcv"
right_keys = "yuiophjklbnm"

dict = {}

for i in range(len(line_one)):
    dict[line_one[i]] = [0, i]

for i in range(len(line_two)):
    dict[line_two[i]] = [1, i]

for i in range(len(line_three)):
    dict[line_three[i]] = [2, i]

sl, sr = input().split()
word = input()

old_l = dict[sl]
old_r = dict[sr]
time = 0
for s in word:
    if s in left_keys:
        cur_l = dict[s]
        distance = abs(cur_l[0] - old_l[0]) + abs(cur_l[1] - old_l[1])
        old_l = cur_l
        time += distance
    else:
        cur_r = dict[s]
        distance = abs(cur_r[0] - old_r[0]) + abs(cur_r[1] - old_r[1])
        old_r = cur_r
        time += distance
    time += 1

print(time)
