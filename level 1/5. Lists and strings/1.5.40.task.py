def my_f(digit):
    result_list = []
    znaki = ["*", "/", "^", "-", "+"]
    temp = ""
    for i in digit:        
        if i not in znaki:
            temp += i
        elif i in znaki:
            temp = float(temp)
            result_list.append(temp)
            result_list.append(i)
            temp = ""
    if len(temp) > 0:
        result_list.append(float(temp))
    return result_list


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