with open("file_3.txt", "r") as f:
    pay = 0
    count = 0
    for line in f:
        list_1 = line.split(" ")
        pay = pay + int(list_1[1])
        count+=1
        if int(list_1[1]) >= 20000:
            print(list_1[0])
print(f"Средняя заработная плата составляет:{pay/count} ")