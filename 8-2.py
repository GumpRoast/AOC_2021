from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/8_input.txt'

with open(file_path) as f:
    in_file = [line.strip().split('|') for line in f]

#for item in in_file:
    #print(item)
output = []
for item in in_file:
    output.append(item[1])
print(output)

count = 0

for item in output:
    # break out each string (i.e. each digit to be lit)
    first, second, third, fourth = item.strip().split(' ')
    # check if it's a 1 (len 2), 4 (len 4), 7 (len 3), or 8 (len 7)
    if len(first) == 2 or len(first) == 4 or len(first) == 3 or len(first) == 7:
        count += 1
    if len(second) == 2 or len(second) == 4 or len(second) == 3 or len(second) == 7:
        count += 1
    if len(third) == 2 or len(third) == 4 or len(third) == 3 or len(third) == 7:
        count += 1
    if len(fourth) == 2 or len(fourth) == 4 or len(fourth) == 3 or len(fourth) == 7:
        count += 1
print(count)