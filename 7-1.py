from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/7_input.txt'

with open(file_path) as f:
    for line in f:
        positions = line.split(',')
        positions = [int(item) for item in positions]

# get the median position
positions.sort()
middle = int(len(positions)/2)

# print(positions[middle])

# leading up to the median and from median to last position
# add up total fuel to get to the median
fuel = 0 
for item in positions[0:middle]:
    fuel += abs(positions[middle] - item)
for item in positions[middle:]:
    fuel += abs(positions[middle] - item)

print(fuel)