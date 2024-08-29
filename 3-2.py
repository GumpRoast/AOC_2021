from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/3_input.txt'

# O-2 Gen

count_0 = 0
count_1 = 0
my_list = []
new_list = []

with open(file_path, 'r') as f:
    # find most common bit
    for line in f:
        my_list.append(line.strip())

for x in range(12):
    for line in my_list:
        if line[x] == '0':
            count_0 += 1
        elif line[x] == '1':
            count_1 += 1

    if count_0 > count_1:
        for line in my_list:
            if line[x] == '0':
                new_list.append(line)
    elif count_0 < count_1 or count_0 == count_1:
        for line in my_list:
            if line[x] == '1':
                new_list.append(line)

    #print(count_1, count_0)
    count_0 = 0
    count_1 = 0
    #print(my_list)
    #print(new_list)
    my_list = new_list
    new_list = []
print(my_list)

o2 = int(''.join(map(str, my_list)))

count_0 = 0
count_1 = 0
my_list = []
new_list = []

with open(file_path, 'r') as f:
    # find most common bit
    for line in f:
        my_list.append(line.strip())

for x in range(12):
    for line in my_list:
        if line[x] == '0':
            count_0 += 1
        elif line[x] == '1':
            count_1 += 1

    if count_0 < count_1 or count_0 == count_1:
        for line in my_list:
            if line[x] == '0':
                new_list.append(line)
    elif count_0 > count_1:
        for line in my_list:
            if line[x] == '1':
                new_list.append(line)
    if count_0 == 0 or count_1 == 0:
        break
    #print(x)
    #print(count_1, count_0)
    count_0 = 0
    count_1 = 0
    #print(new_list)
    #print(new_list)
    my_list = new_list
    new_list = []
print(my_list)

co2 = int(''.join(map(str, my_list)))

answer = int(str(o2), 2) * int(str(co2), 2)
print(answer)