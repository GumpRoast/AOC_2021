from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/6_ex.txt'

with open(file_path) as f:
    for line in f:
        start = line.split(',')
        start = [int(item) for item in start]

fish = [0,0,0,0,0,0,0,0,0]

for i in range(len(start)):
    if start[i] == 0:
        fish[0] += 1
    if start[i] == 1:
        fish[1] += 1
    if start[i] == 2:
        fish[2] += 1
    if start[i] == 3:
        fish[3] += 1
    if start[i] == 4:
        fish[4] += 1
    if start[i] == 5:
        fish[5] += 1
    if start[i] == 6:
        fish[6] += 1
    if start[i] == 7:
        fish[7] += 1
    if start[i] == 8:
        fish[8] += 1

fish_ = 0
new = False
days = 18
#print(fish)
while days > 0:
    print(fish)
    # decrease the fish timer
    fish_ = fish[0] 
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7]
    fish[7] = fish[8]
    if fish_ > 0:
        fish[6] += fish_
        fish[8] += fish_

    days -= 1
