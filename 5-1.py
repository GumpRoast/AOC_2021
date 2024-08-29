from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/5_ex.txt'

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
for i in range(len(x_1)):
    grid.append([0 for i in range(len(x_1))])
    
start  = list(zip(x_1, y_1))
end  = list(zip(x_2, y_2))
print()
print(start)
print(end)
print()

#for z in range(10):
for i in range(len(grid)):
    # straight vertical line
    if x_1[i] == x_2[i]:
        for j in range(y_1[i], y_2[i]):
            grid[j][x_1[i]] += 1
    # straight horizontal line
    if y_1[i] == y_2[i]:
        for j in range(x_1[i], x_2[i]):
            grid[y_1[i]][j] += 1
for item in grid:
    print(item)
