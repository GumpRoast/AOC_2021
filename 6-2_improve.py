from pathlib import Path

# Open the damn file in WSL
path = str(Path(__file__).parent)
file_path = path + '/6_input.txt'

with open(file_path) as f:
    for line in f:
        start = line.split(',')
        start = [int(item) for item in start]

fish = [0,0,0,0,0,0,0,0,0]

# Build the starting list of fish
# 
# The index of the list represents the number of days left in any fish's timer
# 
# The value at the index of the list represents 
# the number of fish with that index's timer value
for i in range(len(start)):
    for j in range(len(fish)):
        if start[i] == j:
            fish[j] += 1

# The number of fish at Day 0; used to backup the number of fish with 0 days in their timer
fish_ = 0

# Number of days that elapse
days = 80

# Main loop to simulate number of days that elapse
while days > 0:
    # decrease the fish timer
    fish_ = fish[0] 
    for i in range(8):
        fish[i] = fish[i + 1]
    # reset 0 timer fish to 6 timer fish
    fish[6] += fish_
    # generate new 8 timer fish based on number of 0 timer fish
    fish[8] = fish_
    # count the days down
    days -= 1

# Sum up the fish on that day
sum = 0 
for item in fish:
    sum += item

print(sum)