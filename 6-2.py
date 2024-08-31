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

new = False
days = 6
#print(fish)
while days > 0:
    print(fish)
    
    if fish[0] > 0:
        new = True
    if fish[1] > 0:
        fish[0] = fish[1]
        fish[1] = 0
    if fish[2] > 0:
        fish[1] = fish[2]
        fish[2] = 0
    if fish[3] > 0:
        fish[2] = fish[3]
        fish[3] = 0
    if fish[4] > 0:
        fish[3] = fish[4]
        fish[4] = 0
    if fish[5] > 0:
        fish[4] = fish[5]
        fish[5] = 0
    if fish[6] > 0 and new == False:
        fish[5] = fish[6]
        fish[6] = 0
    if fish[7] > 0:
        fish[6] = fish[7]
        fish[7] = 0
    if fish[8] > 0 and new == False:
        fish[7] = fish[8]
        fish[8] = 0
    if new == True:
        fish[6] += fish[0]
        fish[8] += fish[0]
        fish[0] = 0
        new = False
    
    days -= 1
