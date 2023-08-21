import random as rd
a = open("./1.7.1.txt")                 # прочитаем в буфер текстовый файл
s = a.readlines()                       # создадим список строк
s = [i.strip() for i in s]              # уберём пробелы, табуляции, перенос строк 
print(s)
print()

# теперь выведем случайную строку, по сути случайный элемент из списка
number_str = rd.randint(0, (len(s) - 1))
print(s[number_str])