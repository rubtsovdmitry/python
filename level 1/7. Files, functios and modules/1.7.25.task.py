def my_function(x):
    x = x.strip()
    if x.isdigit():
        return "Это цифра."
    else:
        return "Это не цифра."


x = input("%80s" % "Введите символы и программа проверит цифры это или нет: ")
print("%79s" %  my_function(x))