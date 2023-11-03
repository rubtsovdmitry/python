from sys import argv                            

script, first = argv         
buf = open(f"./{first}", "r")       
text = buf.readline()                               # считываем данные из файла по-строчно
count = 1
result = ""
while text != "":
    new_str = str(count) + ": " + text
    count += 1
    result += new_str
    text = buf.readline()                           # продолжаем считывать данные из файла по-строчно, пока строка не будет равна ""
print(result)