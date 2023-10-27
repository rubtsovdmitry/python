def my_f2(result_list):
    uno_list = []
    znaki = ["*", "/", "^", "-", "+"]
    znaki_2 = ["-", "+"]
    temp = ""
    for index, i in enumerate(result_list):
        if index == 0 and i in znaki_2:
            uno_list.append("u" + i)
            temp = i
        elif i not in znaki_2:
            uno_list.append(i)
            temp = i
        elif i in znaki_2 and temp in znaki:
            uno_list.append("u" + i)
            temp = i
        elif i in znaki_2 and temp not in znaki:
            uno_list.append(i)
            temp = i    
    return uno_list  


def my_f(digit):
    result_list = []
    znaki = ["*", "/", "^", "-", "+"]
    temp = ""
    for i in digit:
        if i == " ":
            pass
        elif i in znaki:
            result_list.append(temp)
            result_list.append(i)
            temp = ""
        elif i not in znaki:
            i = float(i)
            i = str(i)
            temp += i
    if len(temp) > 0:
        result_list.append(float(temp))
    result_list = [i for i in result_list if i != ""]
    return (my_f2(result_list))
        

# ввод данных
while True:
    digit = input("%100s" % "Введите математическое выражение: ")
    try:
        result_list = my_f(digit)         
        break
    except:
        print("%99s" % "Вы ввели не цифры с операторами.")
        print()

print(result_list)