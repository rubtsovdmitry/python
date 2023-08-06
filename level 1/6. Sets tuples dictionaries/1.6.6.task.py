money = 500

month = input("Введите название месяца: ")
days31 = set({"january", "march", "may", "july", "august", "october", "december"})
days30 = set({"april", "june", "september", "november"})
days28 = set({"february"})

if month in days31:
    print("Количество дней в месяце", 31, "Премия составила", (31 * 500), "руб.")
elif month in days30:
    print("Количество дней в месяце", 30, "Премия составила", (30 * 500), "руб.")
elif month in days28:
    print("Количество дней в месяце", 28, "Премия составила", (28 * 500), "руб.")
else:
    print("Месяц введён с ошибкой")