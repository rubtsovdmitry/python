from sys import argv                            

script, first = argv         
buf = open(f"./{first}", "r")       
text = buf.readlines()                                              # нужно разбить текст на список строк
text = [i.rstrip() for i in text]                                   # уберём знаки переноса в конце строк

result_list = []                                                    # в этот список накопим только каждое слово по отдельности
for i in text:
    temp = i.split(" ")
    result_list.extend(temp)

longest = len(max(result_list, key=len))                            # определим длину самого длинного слова
result_list = [i for i in result_list if len(i) == longest]         # отберём все слова с самой большой длиной

print()
for i in result_list:
    print(i)
print()