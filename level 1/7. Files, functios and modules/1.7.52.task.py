buff = open("./pushkin_mistakes.txt")

text_before = []                                                                                    # будем сюда сохранять предыдущую строку
count = 0                                                                                           # счётчик строк
mistake = []                                                                                        # в этот список будем кидать номера строк с ошибками
while True:
    count += 1
    text = buff.readline()
    if text == "":                                                                                  # условие отмены цикла
        break
    text = text.lower()
    text_mod = ""                                                                                   # создаём новую строку с нуля
    for i in text:
        if ("а" <= i <= "я") or (i == " ") or (i == "-"):
            text_mod += i
    text = text_mod.split(" ")                                                                      # разобьём новую строку на список из слов
    text = [i for i in text if (i != "")]                                                           # уберём лишнее из списка
    if len(text_before) > 0 and len(text) > 0:                                                      # ищем ошибки-повторы в разных строках
        if text[0] == text_before[-1]:
            mistake.append(count)        
    temp = ""                                                                                       # ищем ошибки-повторы в одной строке
    for i in text:
        if i == temp:
            mistake.append(count)
        temp = i
    print(count, text)                                                                              # напечатаем строки-списки и их номера, для проверки
    text_before = text                                                                              # присвоем новое значение для предыдущей строки

print()
print("Ошибки в след. строках (если номера повторяются значит несколько ошибок):", mistake)
print()