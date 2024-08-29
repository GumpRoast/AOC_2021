from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/5_ex.txt'

with open(file_path) as f:
    in_file = [item for item in f]

x_1 = [line.strip().split('->').pop(0).split(',').pop(0).strip() for line in in_file]
y_1 = [line.strip().split('->').pop(0).split(',').pop(1).strip() for line in in_file]
x_2 = [line.strip().split('->').pop(1).split(',').pop(0).strip() for line in in_file]
y_2 = [line.strip().split('->').pop(1).split(',').pop(1).strip() for line in in_file]
    #x_1 = [line.strip().split('->').pop(0).split(',').pop() for line in f]
    #x_1 = [line.strip().split('->').pop(0).split(',').pop(0) for line in f]
    #x_1 = [line for line in f]
#print(in_file)
print(x_1)
print(y_1)
print(x_2)
print(y_2)
grid = []
for i in range(9):
    grid.append(['.' for i in range(len(x_1))])
    

for i in range(len(x_1)):
    if x_1[i] == x_2[i]:
        grid[i] = 1
    if y_1[i] == y_2[i]:
        ...

for item in grid:
    print(item)