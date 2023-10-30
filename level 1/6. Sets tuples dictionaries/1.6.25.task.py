# ввод данных
things_dict = {
    "верёвка": 1,
    "факел": 6,
    "золотая монета": 42,
    "кинжал": 1,
    "стрела": 12
}
dragon_craft = [ "золотая монета", "кинжал", "золотая монета", "золотая монета", "рубин"]

# обновим словарь новыми данными
for i in dragon_craft:
    if i not in things_dict:
        things_dict[i] = 1
    else:
        things_dict[i] += 1

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
