# ввод данных
data = [["яблоки", "апельсины", "вишни", "бананы"], ["Алиса", "Боб", "Кэрол", "Дэвид"], ["собаки", "кошки", "лось", "гусь"]]
for i in range(50):
    print("_", end="")
print("\n")
for a, b, c in zip(data[0], data[1], data[2]):
    print(a.rjust(10), b.rjust(10), c.rjust(10))
for i in range(50):
    print("_", end="")
print("\n")