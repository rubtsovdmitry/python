import time

def my_print(indent):                                       # все эти принты функция печатает в одну строку 
    print(" " * indent, end="")
    print("Hello, world!!!" , end="")
    print(" " * 10, end="")
    print("Hello, world!!!" , end="")
    print(" " * 10, end="")
    print("Hello, world!!!" , end="")
    print(" " * 10, end="")
    print("Hello, world!!!")


indent = 0                                                  # будем копить и уменьшать значение для пробелов циклично
indent_move = True                                          # маркер направления движения строки

while True:        
    if indent_move:                                         # если маркер растущий, то количество пробелов увеличивается
        my_print(indent)                                    # передаём функции новое значение пробелов
        indent += 1
        if indent == 50:                                    # при 50 пробелов маркер меняет направление
            indent_move = False
    else:                                                   # маркер уменьшается
        my_print(indent)
        indent -= 1
        if indent == 0:
            indent_move = True                              # при 0 пробелов маркер меняет направление
    time.sleep(0.1)                                         # задержка перед выполнением следующего действия 