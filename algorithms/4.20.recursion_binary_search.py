"""Реализация бинарного поиска с помощью рекурсии."""

def bin_seek(digit_for_seek, diapazon):
    if int((min(diapazon) + max(diapazon) - 1) / 2 + 0.5) == digit_for_seek:
        return [digit_for_seek, 1]
    else:       
        if (int((min(diapazon) + max(diapazon) - 1) / 2) + 0.5) > digit_for_seek:
            diapazon = range(min(diapazon), int((min(diapazon) + max(diapazon) - 1) / 2 + 0.5))
        else:
            diapazon = range((int((min(diapazon) + max(diapazon) - 1) / 2 + 0.5) + 1), max(diapazon) + 1)
        temp = bin_seek(digit_for_seek, diapazon)                                                               # спиоск [10, 1], где первый элемент - искомая цифра, а второй - это счётчик попыток
        return [temp[0], (temp[1] + 1)]


# входящие данные
diapazon = range(1, 101)                                                                                        # диапазон цифр
digit_for_seek = 2                                                                                              # искомая цифра

check = bin_seek(digit_for_seek, diapazon)

print()
print("Test ok." if digit_for_seek == check[0] else "The test failed.")
print(f"Число угадано с {check[-1]} попытки.")