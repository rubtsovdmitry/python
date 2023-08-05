# первый вариант
diapazon = range(20, 101)
for i in diapazon:
    if i % 5 == 0:
        print(i)
print()

# второй вариант
diapazon = range(20, 101)
result = [i for i in diapazon if i % 5 == 0]    # пока ещё темы списков не было, забегая вперёд, вот такое решение (для списков своя запись для циклов с условием)
print(result)