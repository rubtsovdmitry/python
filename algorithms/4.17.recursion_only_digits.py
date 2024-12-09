def my_def(text):
    if text == "":
        return ""
    else:
        temp = text[0] if text[0].isdigit() else ""
        result = temp + my_def(text[1:])
    return result


text = input("%100s" % "Введите строку: ")
print("%99s" % f"Цифры в строке: {my_def(text)}.")