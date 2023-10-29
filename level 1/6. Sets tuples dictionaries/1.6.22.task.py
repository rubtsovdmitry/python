import pprint

def my_f(guests):
    done = {}
    for a in guests.values():
        for b, c in a.items():
            if b not in done:
                done[b] = c
            else:
                done[b] += c
    return done


# ввод данных
guests = {
    "Дмитрий": {"яблоки": 5, "конфеты": 12},
    "Ольга": {"бутерброды": 3, "яблоки": 2},
    "Мария": {"чашки": 4, "пироги": 1},
    "Михаил": {"бананы": 4, "вода": 6}
}

result = my_f(guests)
print()
pprint.pprint(result)                           # красивый вывод словаря на печать
print()