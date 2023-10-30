# ввод данных
things_dict = {
    "верёвка": 1,
    "факел": 6,
    "золотая монета": 42,
    "кинжал": 1,
    "стрела": 12
}

# печать горизонтальной линии
print()
for i in range(0, 15):
    print("_", end=" ")
print("\n")

print("Инвентарь:")
print()

# печать списка вещей
for a, b, in things_dict.items():
    print("   ", "%15s" % a, "  -  ", b)

print()
print("Всего элементов:", sum(things_dict.values()))

# печать горизонтальной линии
print()
for i in range(0, 15):
    print("_", end=" ")
print("\n")