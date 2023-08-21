import math as mt                       # импортируем библиотеку как псевдоним mt

# ввод данных
trigonometry = ("sin", "cos", "tg", "ctg")
degrees = (0, 30, 45, 60, 90, 180, 270, 360)

# переведём градусы в радианы, градусы и радианы будут одинаковой длины и их далее будет легко обойти в цикле с помощью zip
degrees_radians = [mt.radians(i) for i in degrees]

# создадим и заполним словарь тригонометрических функций
table_trigonometry = dict()
for i in trigonometry:
    for i2, i3 in zip(degrees, degrees_radians):
        if i == "sin":            
            table_trigonometry[i + " " + str(i2)] = round(mt.sin(i3), 3)                                                            # заполним словарь для синуса
        elif i == "cos":
            table_trigonometry[i + " " + str(i2)] = round(mt.cos(i3), 3)                                                            # заполним словарь для косинуса
        elif i == "tg":          
            table_trigonometry[i + " " + str(i2)] = "None" if i2 == 90 or i2 == 270 else round(mt.tan(i3), 3)                       # заполним словарь для тангенса. Кстати можно было использовать тип данных из модуля math "nan"
        else:
            table_trigonometry[i + " " + str(i2)] = "None" if i2 ==0 or i2 == 180 or i2 == 360 else round(1 / mt.tan(i3), 3)        # заполним словарь для котангенса

# избавимся от знака "-" у нуля (он вылезет при расчётё)
for i, i2 in table_trigonometry.items():    
    if type(i2) is not str and mt.isclose(i2, 0, abs_tol=0.0001) is True:                                                           # проверяем являются ли значения близкими. если будет тип "nan", то было бы проще
        table_trigonometry[i] = 0.0

# создадим для каждой тригонометрической функции свой словарь и запишем данные в файл
f = open("./1.7.3.txt", "a")
sinus = dict()
for i, i2 in table_trigonometry.items():
    if "sin" in i:
        sinus[i] = i2        
        a = (f"{i:.>8}", f"{i2:.>8}")
        print(a, end="|")
        f.write(str(a))
b = "\n"                                                                                                                            # создана переменная для переноса строки, чтобы файл получался красивым
f.write(b)
print()

cosinus = dict()
for i, i2 in table_trigonometry.items():
    if "cos" in i:
        cosinus[i] = i2
        a = f"{i:.>8}", f"{i2:.>8}"
        print(a, end="|")
        f.write(str(a))
b = "\n"
f.write(b)
print()

tangens = dict()
for i, i2 in table_trigonometry.items():
    if i[0:2] == "tg" in i:
        tangens[i] = i2
        a = f"{i:.>8}", f"{i2:.>8}"
        print(a, end="|")
        f.write(str(a))
b = "\n"
f.write(b)
print()

cotangens = dict()
for i, i2 in table_trigonometry.items():
    if "ctg" in i:
        cotangens[i] = i2
        a = f"{i:.>8}", f"{i2:.>8}"
        print(a, end="|")
        f.write(str(a))
b = "\n"
f.write(b)
print()

f.close()