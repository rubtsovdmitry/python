estimation = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0,
}
letter = input("%50s" % "Введите буквенную оценку: ")

if letter in estimation:                     
    print("%49s" % "Ваша оценка:", estimation[letter])
else:
    print("%49s" % "Такой оценки нет")