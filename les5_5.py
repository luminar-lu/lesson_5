with open("file_5.txt", "w") as f:
    f.write("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")
with open("file_5.txt", "r") as f:
    a = f.read()
    list_1 = a.split(" ")
    sum = 0
    for i in range(len(list_1)):
        sum = sum + int(list_1[i])

print(sum)