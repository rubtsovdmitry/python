# ввод данных
post_index = {
    "A": "Ньюфаундленд",
    "B": "Новая Шотландия",
    "C": "Остров Принца Эдуарда",
    "E": "Нью-Брансуик",
    "G": "Квебек",
    "H": "Квебек",
    "J": "Квебек",
    "K": "Онтарио",
    "L": "Онтарио",
    "M": "Онтарио",
    "N": "Онтарио",
    "P": "Онтарио",
    "R": "Манитоба",
    "S": "Саскачеван",
    "T": "Альберта",
    "V": "Британская Колумбия",
    "X": "Нунавут или Северо-Западные территории",                                                  # здесь ключу соответствуют две территории (не может быть два одинаковых ключа)
    "Y": "Юкон"
}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

print()
while True:
    index = input("%100s" % "Введите индекс Канады (6 символов): ")
    index = index.upper()    
    if len(index) != 6:
        print("%99s" % "Индекс не той длины.")
    elif index[0] not in alphabet and index[2] not in alphabet and index[4] not in alphabet:
        print("%99s" % "Первый, третий или пятый символ не буква.")
    elif index[1] not in digits and index[3] not in digits and index[5] not in digits:
        print("%99s" % "Второй, четвёртый или шестой символ не цифра.")  
    elif index[0] not in post_index:                                                                # внимательно, есть буквы, кот. не соответствуют ни одной провинции
        print("%99s" % "Первый символ не соответствует ни одной провинции.")
    elif index[1].isdigit() == False:
        print("%99s" % "Второй символ не соответствует ни одной территории в провинции.")
    elif index[1] == "0":
        print("%99s" % f"Это провинция: {post_index[index[0]]}. Сельская местность.")
        break
    elif index[1] in "123456789":
        print("%99s" % f"Это провинция: {post_index[index[0]]}. Городская территория.")
        break