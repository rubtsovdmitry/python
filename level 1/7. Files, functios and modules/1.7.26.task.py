def my(operator):
    my_dict = {
        1: ("+", "-"),
        2: ("*", "/"),
        3: ("^")
    }
    result = "такого оператора нет"
    for a, b in my_dict.items():
        if operator in b:
            result = str(a)                            
    return result
        

operator = input("%75s" % """Введите оператор "+", "-", "*", "/" или "^": """)
print("%74s" % "Приоритет для оператора:", f"{my(operator)}.")