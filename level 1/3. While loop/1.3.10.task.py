def price(tickets, age):
    for a, b in tickets.items():
        if age in b:
            price = float(a.removesuffix("$"))
    return price


tickets = {
    "0$": range(0, 3),
    "12$": range(3, 13),
    "18$": range(65, 100),
    "23$": range(13, 65)
}

amount = 0
while True:
    age = input("%75s" % "Введите возраст посетителя (количество полных лет): ")
    if age == "":
        break
    try:
        age = int(age)
        amount += price(tickets, age)
    except:
        print("%74s" % "Введены некорректные данные.")
print("%74s" % "Общая цена билетов: ", round(amount, 2), "$")