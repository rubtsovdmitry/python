proposal = input("%100s" % "Введите предложение: ")
my_list = proposal.split(" ")   

znaki = [".", ",", "!", "?"]
glasnie = ["a", "e", "i", "o", "u"]
soglasnie = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
y = ["y"]

glasnie_up = [i.upper() for i in glasnie]
soglasnie_up = [i.upper() for i in soglasnie]
y_up = [i.upper() for i in y]

result = []
for i in my_list:
    if (i[0] in glasnie or i[0] in glasnie_up) and i[-1] not in znaki:                   # если первая буква слова гласная и после слова нет знаков препинания
        result.append(i + "way")    
    elif (i[0] in glasnie or i[0] in glasnie_up) and i[-1] in znaki:                     # если первая буква слова гласная и после слова есть знак препинания
        i = list(i)
        i.insert(-1, "way")
        i = "".join(i)
        result.append(i)
    ###############################################################################################################################################################################    
    elif i[0] in soglasnie and i[-1] not in znaki:                                       # если первая буква слова coгласная и маленькая и после слова нет знаков препинания
        temp = str()
        temp_result = str()
        flag = 0
        for x in i:            
            if x in soglasnie and flag == 0:
                temp += x
            elif x not in soglasnie and flag == 0:
                flag = 1
                temp_result += x
            else:
                temp_result +=x
        temp_result += (temp + "ay")                    
        result.append(temp_result)
    elif i[0] in soglasnie_up and i[-1] not in znaki:                                   # если первая буква слова согласная и большая и после слова нет знаков препинания
        i = i.lower()
        temp = str()
        temp_result = str()
        flag = 0
        for x in i:            
            if x in soglasnie and flag == 0:
                temp += x
            elif x not in soglasnie and flag == 0:
                flag = 1
                temp_result += x
            else:
                temp_result +=x
        temp_result += (temp + "ay")                    
        temp_result = [i for i in temp_result]
        temp_result[0] = temp_result[0].upper()
        temp_result = "".join(temp_result)
        result.append(temp_result)
    ###############################################################################################################################################################################
    elif i[0] in soglasnie and i[-1] in znaki:                                          # если первая буква слова согласная и маленькая и после слова есть знак препинания
        temp_znak = i[-1]
        i = i[0:-1]
        temp = str()
        temp_result = str()
        flag = 0
        for x in i:            
            if x in soglasnie and flag == 0:
                temp += x
            elif x not in soglasnie and flag == 0:
                flag = 1
                temp_result += x
            else:
                temp_result +=x
        temp_result += (temp + "ay" + temp_znak)                    
        result.append(temp_result)    
    elif i[0] in soglasnie_up and i[-1] in znaki:                                       # если первая буква слова согласная и большая и после слова есть знак препинания
        i = i.lower()
        temp_znak = i[-1]
        i = i[0:-1]
        temp = str()
        temp_result = str()
        flag = 0
        for x in i:            
            if x in soglasnie and flag == 0:
                temp += x
            elif x not in soglasnie and flag == 0:
                flag = 1
                temp_result += x
            else:
                temp_result +=x
        temp_result += (temp + "ay" + temp_znak)                    
        temp_result = [i for i in temp_result]
        temp_result[0] = temp_result[0].upper()
        temp_result = "".join(temp_result)
        result.append(temp_result)
        ###############################################################################################################################################################################
    elif (i[0] in y or i[0] in y_up) and i[-1] not in znaki:                             # если первая буква слова гласная и после слова нет знаков препинания
        result.append(i + "ay")    
    elif (i[0] in y or i[0] in y_up) and i[-1] in znaki:                                 # если первая буква слова гласная и после слова есть знак препинания
        i = list(i)
        i.insert(-1, "ay")
        i = "".join(i)
        result.append(i)

result = " ".join(result)
print("%99s" % result)