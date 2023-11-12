def my_def(data):
    if len(data) == 0:
        return 0
    temp = data[1:]
    amount = data[0] + my_def(temp)
    return amount


data = [0, 1, 2, 3, 2, 1, 0, 6]
print(my_def(data))