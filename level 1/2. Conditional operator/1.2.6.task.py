#################################   1-й способ

letter = input("%50s" % "Введите латинскую букву: ")
letter = letter.lower()

if letter == "y":
    print("%49s" % "Эта буква может быть и гласной и согласной.")
elif letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("%49s" % "Эта буква гласная.")
else:
    print("%49s" % "Эта буква согласная.")

#################################   2-й способ

letter = input("%50s" % "Введите латинскую букву: ")
letter = letter.lower()

GLAS_SOGLAS = ["y"]
GLASS = ["a", "e", "i", "o", "u"]

result = "Эта буква может быть и гласной и согласной." if letter in GLAS_SOGLAS else ("Эта буква гласная." if letter in GLASS else "Эта буква согласная.")      # запись вложенного условия в одну строку
print("%49s" % result)