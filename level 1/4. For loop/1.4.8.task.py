number = input("Введите большоее целое число: ")
amount = 0
for i in number:
    amount += int(i)
print("Сумма цифр в этом числе равно", amount)