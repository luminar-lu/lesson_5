with open("file_2.txt", "r") as f:
    count = 0
    for line in f:
        a = line.split( )
        count += 1
        print(f" Количество слов в {count} строке: {len(a)}.")
