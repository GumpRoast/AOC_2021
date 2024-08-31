from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/6_ex.txt'

with open(file_path) as f:
    for line in f:
        start = line.split(',')
        start = [int(item) for item in start]

new_fish = 0
days = 19

while days > 0:
    print(start)
    # day passes
    for i in range(len(start)):
        if start[i] != 6 or start[i] != 8:
            start[i] -= 1
    # check if any timers run out
    for i in range(len(start)):
        if start[i] == -1:
            start[i] = 6
            start.append(int(8))
    days  -= 1

print(len(start))