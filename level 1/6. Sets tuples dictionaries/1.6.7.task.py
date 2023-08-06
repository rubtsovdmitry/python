# входные данные
enter_data = input("Введите строку: ")

# обойдем наш текст в цикле, и если значений цикла нет в новом словаре, то добавляем, если есть, то +1
result_dict = dict()
for i in enter_data:
    if i not in result_dict:
        result_dict[i] = 1
    elif i in result_dict:
        result_dict[i] += 1
print(result_dict)