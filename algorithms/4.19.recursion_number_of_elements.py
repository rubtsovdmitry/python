def count_function(a):
    if len(a) == 0:
        return 0
    else:
        a.pop()
        count = 1 + count_function(a)
        return count
    

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_digits = count_function(a)

print(f"Количество элементов списка: {count_digits}.")