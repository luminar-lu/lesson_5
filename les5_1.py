with open("file.txt", "w") as f:
    while True:
        a = input("Введите строчку (пустая строка для прекращения работы программы) : ")
        f.write(a + "\n")
        if len(a) == 0:
            break

