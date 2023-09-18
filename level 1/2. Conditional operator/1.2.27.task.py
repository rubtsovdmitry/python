number = input("%100s" % "Введите гос. номер автомобиля: ")

if len(number) == 6 and \
  number[-3:-1].isdigit() == True and \
  "А" <= number[0] <= "Я" and \
  "А" <= number[1] <= "Я" and \
  "А" <= number[2] <= "Я":
    print("%99s" % "Гос. номера старого образца")
elif len(number) == 7 and \
  number[0:4].isdigit() == True and \
  "А" <= number[4] <= "Я" and \
  "А" <= number[5] <= "Я" and \
  "А" <= number[6] <= "Я":
    print("%99s" % "Гос. номера нового образца")
else:
    print("%99s" % "Неверный формат гос. номера")