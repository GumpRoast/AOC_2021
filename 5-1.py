from pathlib import Path
import array as a

path = str(Path(__file__).parent)
file_path = path + '/5_ex.txt'

total = 0 

with open(file_path) as f:
    in_file = [item for item in f]

x_1 = [int(line.strip().split('->').pop(0).split(',').pop(0).strip()) for line in in_file]
y_1 = [int(line.strip().split('->').pop(0).split(',').pop(1).strip()) for line in in_file]
x_2 = [int(line.strip().split('->').pop(1).split(',').pop(0).strip()) for line in in_file]
y_2 = [int(line.strip().split('->').pop(1).split(',').pop(1).strip()) for line in in_file]

print(x_1)
print(x_2)
print(y_1)
print(y_2)

grid = []

rows, cols = len(x_1), len(y_1)
grid = [[0] * cols] * rows
print(grid)
#for i in range(len(x_1)):
#    grid.append([0 for i in range(len(x_1))])
    
start  = list(zip(x_1, y_1))
end  = list(zip(x_2, y_2))
print()
print(start)
print(end)
print()

for i in range(len(x_1)):
    if x_1[i] == x_2[i]:
<<<<<<< HEAD
        for j in range(y_1[i], y_2[i]):
            grid[j][x_1[i]] += 1
    # straight horizontal line
    if y_1[i] == y_2[i]:
        for j in range(x_1[i], x_2[i]):
            grid[y_1[i]][j] += 1
for item in grid:
    print(item)
=======
        if y_1 > y_2:
            
        print('match')

# count the number of intersections
for row in range(len(grid)):
    for col in range(row): 
        if col > 1:
            total += 1
>>>>>>> 986f144 (modified:   5-1.py)
