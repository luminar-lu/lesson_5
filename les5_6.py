dict_1 = {}
with open("file_6.txt", "r") as f:
    for line in f:
        list_1 = line.split()
        lect = list_1[-3]
        prac = list_1[-2]
        lab = list_1[-1]
        sum = int(lect[0:-6:1]) + int(prac[0:-6:1]) +int(lab[0:-5:1])
        a = [(list_1[0], sum)]
        dict_1.update(a)
print(dict_1)