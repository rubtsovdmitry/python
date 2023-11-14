def my_def(data):
    if len(data) == 0:
        return 0
    temp = data[0] if data[0] % 2 != 0 else (data[0] * (-1))
    amount = temp + my_def(data[1:])
    return amount
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("%99s" % f"Результат равен {my_def(data)}.")