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

print(positions[middle])
print(middle)
print(positions)
# leading up to the median and from median to last position
# add up total fuel to get to the median
#fuel = 0 
total = []
for i in range(max(positions)):
    fuel = 0 
    tax = 0
    for item in positions:
        fuel += (abs(i - item) + tax)
        for j in range(abs(i - item)):
            tax += 1
    total.append(fuel)
#print(total)
print(min(total))