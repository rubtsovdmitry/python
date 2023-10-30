# ввод данных
start_dict = {
    1: ".,?!:",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " "
}

# составим словарь с соответствиями для каждого символа
finish_dict = {}
for a, b in start_dict.items():
    count = 0
    for i in b:
        count += 1
        finish_dict[i] = int(count * str(a))

# ввод строки для преобразования
print()
text = input("%100s" % "Введите текст для преобразования: ")
print()

# выведем преобразованный текст 
for i in text:
    i = i.lower()
    if i not in finish_dict:
        print(f"({i})", end="")
    else:
        print(finish_dict[i], end="")
print()
print()