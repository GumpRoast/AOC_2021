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
total_fuel = []
total = 0
fuel = 0
tax = 0

fuel = 0
tax = 0

# for every position
for position in positions:
    if position < middle +1:
        fuel = sum(range((middle + 1) - position))
        total_fuel.append(fuel)
    else:
        fuel = sum(range((position + 1) - middle))
        total_fuel.append(fuel)
print(sum(total_fuel))