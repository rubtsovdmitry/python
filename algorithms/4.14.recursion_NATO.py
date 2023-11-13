def my_def(word):
    if len(word) == 0:
        return ""
    NATO = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu"
    }
    if word[0] in NATO:                                                                         # рекурсивный случай, если в слове буква из алфавита НАТО
        result = (my_def(word[1:]) + " " + NATO[word[0]])
    else:                                                                                       # рекурсивный случай, если в слове символ не из алфавита НАТО
        result = (my_def(word[1:]) + " " + word[0])
    return result


word = input("%100s" % "Введите слово на английском для преобразования: ")
word = list(word[::-1].upper())

print("%99s" % my_def(word).strip())