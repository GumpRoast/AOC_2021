from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/3_input.txt'

line_list = []
big_list = []
final_list = []
count_1 = 0
count_0 = 0

for x in range(12):
    with open(file_path, 'r') as f:
        for line in f:
            if int(line[x]) == 1:
                count_1 += 1
            elif int(line[x]) == 0:
                count_0 += 1
        if count_1 > count_0:
            final_list.append(1)
        else:
            final_list.append(0)
        print(count_1, count_0)
        count_0 = 0 
        count_1 = 0
print(final_list)

flipped_list = []

for item in final_list:
    if item == 1:
        flipped_list.append(0)
    else:
        flipped_list.append(1)

print(flipped_list)

final = int(''.join(map(str, final_list)))
flipped = int(''.join(map(str, flipped_list)))
answer = int(str(final), 2) * int(str(flipped), 2)
print(answer)