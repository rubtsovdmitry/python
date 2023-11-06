buff = open("./pushkin.txt")
text = buff.read()
text = text.lower()

mod_text = ""                                                                               # положим сюда обработанный текст
for i in text:      
    if ("а" <= i <= "я") or (i == " ") or (i == "\n") or (i == "-"):        
        mod_text += i       

mod_text = mod_text.split(" ")                                                              # разобьём текст на слова, каждое слово - это отдельный элемент спсика
mod_text = [i for i in mod_text if (i != "") and ("\n" not in i)]                           # уберём лишнее из списка

count_letters = {}                                                                          # создадим словарь для подсчёта букв
for a in mod_text:                      
    a = set(a)                                                                              # сделаем каждое слово множеством для того, чтобы убрать дубликаты букв
    for b in a:                                                                             # теперь можно копить повторы букв в словаре
        if b not in count_letters:      
            count_letters[b] = 1        
        else:       
            count_letters[b] += 1       
if "-" in count_letters:                                                                    # дефис не относится к буквам, но относится к некоторым словам
    count_letters.pop("-")      

max_count = max(count_letters.values())                                                                                                                     # найдём максимальное количество повторов для каждой буквы в словах
max_letter = [i for i in count_letters if count_letters[i] == max_count]                                                                                    # составим список букв или в нём будет только одна буква, которые попадаются в словах чаще всего
amount_words = len(mod_text)                                                                                                                                # количество слов
print()
for i in max_letter:
    print(f"Буква \"{i}\" встречается в словах чаще всего. Процент слов с этой буквой составляет {round((max_count / amount_words * 100), 2)}%.")
print()