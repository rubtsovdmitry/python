from sys import argv                            # импортируем argv из библиотеки sys (нужно для работы с командной строкой)

try:
    script, first, second, third = argv         # первый параметр - это название скрипта, "first" и "second" - это название файлов, который мы передаём скрипту и последний параметр "third" - в какой файл записываем
    buf_1 = open(f"./{first}", "r")             # читаем данные из файла, путь к файлу состоит из: ./ - читать в тек. каталоге, first - переданное название файла
    str_1 = buf_1.read()                        # превращаем содержимое файла в строку
    buf_2 = open(f"./{second}", "r")
    str_2 = buf_2.read()                        # превращаем содержимое файла в строку
    str_1 += str_2
    output_text = open(f"./{third}", "w")       
    output_text.write(str_1)                    # записываем
    output_text.close()
except:
    print("Вы сделали ошибку в вводе.")