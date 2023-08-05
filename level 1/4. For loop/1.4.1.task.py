# первый вариант
diapazon = range(25, 70)
for i in diapazon:
    print(i)
print()
print("Сумма всех чисел дипазона равна:", sum(diapazon))
print()

# второй вариант
diapazon = range(25, 70)
amount = 0
for i in diapazon:
    amount += i
    print(i)
print()
print("Сумма всех чисел дипазона равна:", amount)