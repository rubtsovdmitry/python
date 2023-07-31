# первый вариант
diapazon = range(20, 101)
for i in diapazon:
    if i % 7 == 0 or i % 9 == 0:
        print(i)
print()

# второй вариант
diapazon = range(20, 101)
result = [i for i in diapazon if i % 7 == 0 or i % 9 == 0]    # для списков своя запись для циклов с условием
print(result)