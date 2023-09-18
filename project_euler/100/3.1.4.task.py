a = range(100, 1000)
b = range(100, 1000)

# составим множество всех возможных произведений
composition_all = set()
for ai in a:
    for bi in b:
        composition_all.add(ai * bi)

# составим список всех возможных палиндромов
composition_palindrom = []
for i in composition_all:
    i = str(i)
    if i == i[::-1]:
        composition_palindrom.append(int(i))

palindrom_max = max(composition_palindrom)

print("%30s" % "Самый большой палиндром:", palindrom_max)