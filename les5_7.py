import json as j
count = 0
summ_profit = 0
dict_profit = {}
dict_waste = {}
with open("file_7.txt", "r") as f:
    for line in f:
        list_1 = line.split(" ")
        profit = int(list_1[-2]) - int(list_1[-1])
        summ_profit += profit
        count += 1
        a = [(list_1[0], profit)]
        if profit > 0:
            dict_profit.update(a)
        else:
            dict_waste.update(a)
    average = summ_profit / count
    dict_average = {'average':average}
    list_1 = [dict_profit, dict_waste, dict_average]
# print(list_1)
with open("file_71.json", 'w') as f:
    j.dump(list_1,f)
