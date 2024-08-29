from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/4_ex.txt'

card_list = []
card = []
winner = []
stop = False
total = 0

with open(file_path) as f:
    cards = [item.strip() for item in f]
    #print(cards)
    called = cards.pop(0).split(',')
    called = [int(item) for item in called]

    for line in cards:
        if not line:
            card_list.append(card)
            card = []
        else:
            line = line.split(' ')
            while '' in line:
                line.remove('')
            line = [int(num) for num in line]
            card.append(line)    
    card_list.pop(0)
    card_list.append(card)

    for num in called:
        for i in range(len(card_list)):
            for j in range(len(card_list[0])):
                for k in range(len(card_list[0][0])):
                    if card_list[i][j][k] == num:
                        card_list[i][j][k] = 'x'
                    
                    if card_list[i][j][0] == 'x' and card_list[i][j][1] == 'x' and card_list[i][j][2] == 'x' and card_list[i][j][3] == 'x' and card_list[i][j][4] == 'x':
                        winner.append(card_list[i])
                        card_list[i] = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]

                        if len(card_list) == len(winner):
                            stop = True

                    if card_list[i][0][k] == 'x' and card_list[i][1][k] == 'x' and card_list[i][2][k] == 'x' and card_list[i][3][k] == 'x' and card_list[i][4][k] == 'x':
                        winner.append(card_list[i])
                        card_list[i] = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]

                        if len(card_list) == len(winner):
                            stop = True
                if stop:
                    break
            if stop:
                break
        if stop:
            mult = num
            break
    
    print(winner[-1])
    print(num)

    for line in winner[-1]:
        for item in line:
            if item != 'x':
                total += item
    print(total)
    total *= mult
    print(total)