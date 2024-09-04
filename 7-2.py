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
total = []
fuel = 0
tax = 0

#middle = 2

fuel = 0
tax = 0

# for every position
for i in range(len(positions)):
    for position in positions:
        if position < i + 1:
            fuel = sum(range((i + 1) - position))
            total.append(fuel)
        else:
            fuel = sum(range((position + 1) - i))
            total.append(fuel)
    total_fuel.append(sum(total))
    total = []
#print(total_fuel)
print(min(total_fuel))