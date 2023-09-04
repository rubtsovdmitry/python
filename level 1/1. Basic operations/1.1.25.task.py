days = int(input("%40s" % "Введите количество дней: "))
hour = int(input("%40s" % "Введите количество часов: "))
minutes = int(input("%40s" % "Введите количество минут: "))
seconds = int(input("%40s" % "Введите количество секунд: "))

print("%39s" % "Всего:", (seconds + minutes * 60 + hour * 60 * 60 + days * 24 * 60 * 60),"секунд")