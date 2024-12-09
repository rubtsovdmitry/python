import random

def get_one_example_plus():                                                                                                                 # плюс
    x = random.randint(100, 899)
    x_str = str(x)
    y = 999
    y_str = str(y)
    while (x + y) > 999 or ((int(x_str[0]) + int(y_str[0])) > 9) or ((int(x_str[1]) + int(y_str[1])) > 9) or ((int(x_str[2]) + int(y_str[2])) > 9):
        y = random.randint(100,899)
        y_str = str(y)
    return [x, "+", y]


def get_one_example_minus():                                                                                                                # минус
    x = random.randint(101, 999)
    x_str = str(x)
    y = 999
    y_str = str(y)
    while (x < y) or (int(x_str[0]) < int(y_str[0])) or (int(x_str[1]) < int(y_str[1])) or (int(x_str[2]) < int(y_str[2])):
        y = random.randint(100,x)
        y_str = str(y)
    return [x, "-", y]


def get_one_example():
    x = random.randint(0, 1)                                                                                                                
    if x == 0:                                                                                                                              # для плюса
        return get_one_example_plus()
    else:                                                                                                                                   # для минуса
        return get_one_example_minus()


buf = open("./6.005.task.txt", "w")
COLUMN = 6                                                                                                                                  # количество столбцов
FIELD = 8                                                                                                                                   # количество строк    

for i in range(FIELD):
    examples_str = []                                                                                                                       # создадим строку примеров
    for i in range(COLUMN):
        examples_str.append(get_one_example())
    for i in range(COLUMN):                                                                                                                 # печать примеров в строку
        s = "%15s" % examples_str[i][0]       
        buf.write(s)
    s = "\n"
    buf.write(s)
    for i in range(COLUMN):
        s = "%11s" % examples_str[i][1]
        buf.write(s)
        s = " ---"
        buf.write(s)
    s = "\n"
    buf.write(s)                
    for i in range(COLUMN):
        s = "%15s" % examples_str[i][2]
        buf.write(s)
    for i in range(4):      
        s = "\n"
        buf.write(s)
    s = ("-" * 90)
    buf.write(s)
    s = "\n"
    buf.write(s)
    
buf.close()