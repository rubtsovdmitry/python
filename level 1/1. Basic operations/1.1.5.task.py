year = int(input("Введите год, чтобы узнать високосный он или нет: "))

result = (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)           # выражение возвращает либо True либо False
print(result)