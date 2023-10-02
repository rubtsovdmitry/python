def new_price(amount):
    amount_in_cents = int(amount * 100)
    need_mod = amount_in_cents % 5 
    need_mod = 0 if need_mod < 2.5 else 5
    amount_in_cents = (amount_in_cents // 5) * 5 + need_mod
    amount = amount_in_cents / 100
    return amount

print("%50s" % "Вводите суммы покупок в формате xx.xx (для отмены введите 0)")
each_price = list()
each_real_price = list()
count = 1
while True:
    amount = float(input("%51s" % f"Введите сумму {count}-й покупки: "))
    if amount == 0:
        break    
    each_price.append(amount)
    each_real_price.append(new_price(amount))
    count += 1

print()
print("%50s%15.2f" % ("Сумма всех покупок без округления равна:", sum(each_price)))
print("%50s%15.2f" % ("Сумма всех покупок с округлением равна:", sum(each_real_price)))