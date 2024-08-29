import os
from pathlib import Path

total = 0
my_list = []
new_list = []
path = str(Path(__file__).parent)
file_path = path + '/1_input.txt'
print(file_path)
with open(file_path, 'r') as f:
    for item in f:
        my_list.append(int(item))
    for i in range(len(my_list) - 2):
        total = my_list[i] + my_list[i+1] + my_list[i+2]
        new_list.append(total)
previous = None
count = 0
for line in new_list:
    if previous == None:
        previous = int(line)
    elif int(line) > previous:
        count += 1
    previous = int(line)
#print(my_list)
#print(new_list)
print(count)