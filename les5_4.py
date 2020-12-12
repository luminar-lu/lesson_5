dict_1 = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
def change():
    with open("file_4_1.txt", "a") as f1:
        f1.write(f'{dict_1[list_1[0]]} {list_1[1]} {list_1[2]}')

with open("file_4.txt", "r") as f:

       for line in f:
           list_1 = line.split(" ")
           change()
