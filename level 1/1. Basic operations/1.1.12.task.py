percent = 4
depozit = float(input("Введите сумму, которую Вы хотите внести на депозит: "))
first_year = depozit + depozit * percent / 100
second_year = first_year + first_year * percent / 100
third_year = second_year + second_year * percent / 100
print("%15s" % "Первый год", "%15s" % "Второй год", "%15s" % "Третий год")
print("%15.2f" % first_year, "%15.2f" % second_year, "%15.2f" % third_year)