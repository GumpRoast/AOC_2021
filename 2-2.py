from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/2_input.txt'

horiz = 0
depth = 0
aim = 0

with open(file_path, 'r') as f:
    for line in f:
        direction, amount = line.strip().split(' ')
        if direction == 'forward':
            horiz += int(amount)
            depth += (aim * int(amount))
        elif direction == 'up':
            aim -= int(amount)
        elif direction == 'down':
            aim += int(amount)

print(depth)
print(horiz)
print(horiz * depth)