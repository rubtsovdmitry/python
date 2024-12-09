my_list = []
while True:
    proposal = input("%100s" % "Введите предложение (просто \"Enter\" для отмены): ")
    if proposal == "":
        break
    if len(my_list) == 0:
        my_list.append(proposal)
    else:
        my_list_len = len(my_list)
        if my_list_len == 1:
            my_list.append("и")            
            my_list.append(proposal)
        elif my_list_len >= 3:
            my_list[-3] = my_list[-3] + ","
            my_list.pop(-2)
            my_list.append("и")            
            my_list.append(proposal)

a = " "
result = a.join(my_list)
print(result)