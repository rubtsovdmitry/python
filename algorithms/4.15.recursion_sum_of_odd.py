def my_def(data):
    if len(data) == 0:
        return 0
    temp = data[0] if data[0] % 2 != 0 else 0
    amount = temp + my_def(data[1:])
    return amount
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("%99s" % f"Сумма всех нечётных чисел в списке равна {my_def(data)}.")