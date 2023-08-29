a = open("./1.7.2.csv", "r")                                                        # прочитаем в буфер файл
s = a.readlines()                                                                   # создадим список строк
s = [i.strip() for i in s]                                                          # уберём пробелы, табуляции, перенос строк 
s = [i.split(",") for i in s]                                                       # разобъём строки в списке и получим список списков 

result = dict()                                         
for i in s:                                                                         # заполним словарь данными из списка
    result[i[0]] = int(i[-1])
print(result, "\n")

amount = 0
for i in result.values():
    amount += i
print("Общее количество посетителей за всё время:", amount, "\n")

srednee = int(amount / len(result) + 0.5)                                           # совершим правильное округление, прибавив 0.5 и отбросив дробную часть 
print("Среднее количество посетителей:", srednee, "\n")

amount = 0
count = 0
for i in result.keys():  
    if i[-2:] == "05":
        amount += result[i]
        count += 1
print("Среднее количество посетителей за май каждого года:", int(amount/count + 0.5))