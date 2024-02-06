"""ПРОГРАММА РЕКУРСИВНО ПЕРЕБИРАЕТ ФАЙЛЫ С РАСШИРЕНИЕМ <jpg>, УКАЗАННЫЕ В КАТАЛОГЕ (это первый аргумент),
ПЕРЕМЕЩАЕТ ИХ В УКАЗАННЫЙ КАТАЛОГ (это второй аргумент) И ПЕРЕИМЕНОВЫВАЕТ ИХ В ВИД 1.jpg ... 1000.jpg"""
import os, pathlib, re, shutil
from sys import argv


try:
    script, one, two = argv                                                                                   # аргументы командной строки
    out_way = pathlib.Path(one)                                                                               # объект-путь, текущее расположение в ФС
    in_way = pathlib.Path(two)                                                                                # объект-путь, место назначения в ФС
except:
    print("Ошибка ввода.")
else:
    regex_obj = re.compile(r".{1,50}\.[Jj][Pp][Gg]")	                                                      # пример шаблона: 1.jpg

    os.makedirs(in_way / "Finish")                                                                            # создадим каталог Finish уровнем выше, в него будем перемещать файлы

    """цикл с функцией os.walk(), который обходит все каталоги и файлы и даже вложенные;
    ПЕРМЕЩАЕМ ФАЙЛЫ"""
    first = 1                                                                                                 # будет меняться значение "first" с каждым каталогом "temp"
    temp = []
    for foldername, subfoldeers, filenames in os.walk(out_way):
        first += len(temp)
        temp = []                                                                                               
        for i in filenames:                                                                                   # для каждого каталога корневого и вложенного свой список файлов, обойдем его в цикле
            b = regex_obj.search(i)                                                                           # сравним файл в списке с выражением REGEX (ищем файла по шаблону)
            if type(b) == re.Match:                                                                           # обрабатываем только подходящие файлы
                temp.append(i)                                                                                # добавляем во временный список подходящие файлы
        amount_files = range(first, first + len(temp))
        for a, b in zip(temp, amount_files):
            original = foldername + "/" + a                                                                   # в переменной хранится полный путь к файлу который нужно переименовать
            clone = in_way / "Finish" / (str(b) + ".jpg")                                                     # в переменной хранится полный путь к файлу который должен получиться
            original = pathlib.Path(original)
            shutil.move(original, clone)
    print("ВЫПОЛНЕНО!!!")