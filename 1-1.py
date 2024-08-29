import os
from pathlib import Path

count = 0
path = str(Path(__file__).parent)
file_path = path + '/1_input.txt'
print(file_path)

with open(file_path, 'r') as f:
    previous = None
    for line in f:
        if previous == None:
            previous = int(line)
        elif int(line) > previous:
            count += 1
        previous = int(line)
print(count)