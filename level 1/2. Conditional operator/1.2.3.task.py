# способ №1

# ввод констант
BUY = 200
TAX = 15

# ввод данных №2 (без проверки)
kurs = float(input("Введите курс евро (в формате xxx.xx): "))
bui_in_rub = float(input("Введите сумму покупки в рублях (в формате xxx.xx): "))

bui_in_eur = bui_in_rub / kurs
if bui_in_eur > 200:
    base_for_tax = bui_in_eur - BUY
    duty_in_eur = TAX / 100 * base_for_tax
    duty_in_rub = duty_in_eur * kurs
else:
    duty_in_rub = 0

print("Размер пошлины для покупки составляет", round(duty_in_rub, 2), "руб.")
print()

###############################################################################################################################

# способ №2 (условие в одну строку)

# ввод констант
BUY = 200
TAX = 15

# ввод данных №2 (без проверки)
kurs = float(input("Введите курс евро (в формате xxx.xx): "))
bui_in_rub = float(input("Введите сумму покупки в рублях (в формате xxx.xx): "))

bui_in_eur = bui_in_rub / kurs

base_for_tax = (bui_in_eur - BUY) if bui_in_eur > 200 else 0

duty_in_eur = base_for_tax * TAX / 100
duty_in_rub = duty_in_eur * kurs

print("Размер пошлины для покупки составляет", round(duty_in_rub, 2), "руб.")