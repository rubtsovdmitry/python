from sys import argv 
import pprint                           

try:
    script, first = argv         
    buf = open(f"./{first}", "r")       
    text = buf.read()                                                   # прочитаем весь текст одним разом
    text = text.replace("-","")
    text = text.replace("\n","")
    text = text.replace(",","")
    text = text.replace(":","")
    text = text.replace(".","")
    text = text.replace(";","")
    text = text.replace("!","")
    text = text.replace("\"","")
    text = text.replace("?","")
    text = text.replace("—","")
    text = text.replace("«","")
    text = text.replace("»","")
    text = text.replace(" ","")
    text = text.replace(" ","")                                        # такой вот пробел был в тексте (пробела выше не хватило)
    text = text.lower()
    
    digits = "0123456789"                   
    for i in digits:                                                   # уберём все цифры из текста
        text = text.replace(i, "")

    result_dict = {}
    for i in text:
        if i not in result_dict:
            result_dict[i] = 1
        else:
            result_dict[i] += 1

    pprint.pprint(result_dict)
except:
    print("Имя файла не существует или слишком много аргументов.")