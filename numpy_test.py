import numpy as np
from pathlib import Path

np.set_printoptions(threshold=np.inf)

def main():
    path = str(Path(__file__).parent)
    file_path = path + '/4_input.txt'

    called = [46,12,57,37,14,78,31,71,87,52,64,97,10,35,54,36,27,84,80,
        94,99,22,0,11,30,44,86,59,66,7,90,21,51,53,92,8,76,41,39,77,42,
        88,29,24,60,17,68,13,79,67,50,82,25,61,20,16,6,3,81,19,85,9,28,56,
        75,96,2,26,1,62,33,63,32,73,18,48,43,65,98,5,91,69,47,4,38,23,49,
        34,55,83,93,45,72,95,40,15,58,74,70,89]

    #a = np.fromfile('4_input.txt', dtype=int)

    #a = np.empty([5, 5], dtype=int)
    card = []
    array = np.zeros((5, 5), dtype=int)
    with open(file_path) as f:
        for line in f:
            my_list = line.strip().split(" ")
            while '' in my_list:
                my_list.remove('')
            #print(my_list)
            
            if my_list == []:
                #print(np.array(card))
                array = np.append(array, np.array(card, dtype=int), axis=0)
                #print(array)
                card = []
            else:
                card.append(my_list)
    print(array)

main()