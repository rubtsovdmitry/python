import random

# функция определяет, какие цифры будут в полях
def my_digit(poryadok):
    temp = {"0":range(1, 10), "1":range(10, 20), "2":range(20, 30), "3":range(30, 40), "4":range(40, 50), "5":range(50, 60), "6":range(60, 70), "7":range(70, 80), "8":range(80, 91)}
    return random.randint(temp[poryadok][0], temp[poryadok][-1])


# функция определяет, какие поля будут заполнены
def my_fields():
    win_dict = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0}
    count = 1
    while count < 6:
        poryadok = str(random.randint(0, 8))
        if win_dict[poryadok] != 0:
            continue
        win_dict[poryadok] = my_digit(poryadok)
        count += 1
    return win_dict


# функция генерирует билет
def generation_ticket():
    return [my_fields(), my_fields(), my_fields()]


# генерация выигрышной строки
win_generate_str_with_fields = my_fields()


# генерация билета
ticket = generation_ticket()
# генерация комбинаций пока не выпадет выигрышная
count = 1
while win_generate_str_with_fields not in ticket:
    ticket = generation_ticket()
    count += 1

# проверим верх, середина или низ
up_middle_down = ticket.index(win_generate_str_with_fields)
if up_middle_down == 0:
    result = "Верх"
elif up_middle_down == 1:
    result = "Середина"
elif up_middle_down == 2:
    result = "Низ"

print(f"Выпал выигрышный билет с {count}-й попытки.")
print(f"На билете совпал(а): {result}.")