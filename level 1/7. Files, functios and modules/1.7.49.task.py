from sys import argv 

try:
    script, first = argv         
    buf = open(f"./{first}", "r")       
    text = buf.readlines()                                                    # прочитаем текст как список строк
    result = []                                                               # сюда накопим новый список без ненужных строк
    for i in text:
        if i[0] != "#" and i[0] != "\n":                                      # выбросим строки, начинающиеся на # и на перенос строки "\n"
            result.append(i)
    buf_out = open(f"./{first}_new", "w")
    temp = ""                                                                 # создадим конечную строку
    for i in result:
        temp += i
    buf_out.write(temp)
    buf_out.close()
except:
    print("Имя файла не существует или слишком много аргументов.")