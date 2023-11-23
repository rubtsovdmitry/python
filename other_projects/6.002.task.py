import pyinputplus

print()
print("Изготовитель бутербродов.")

print()
print("Выберите хлеб. ", end="")
bread = pyinputplus.inputMenu(["Цельнозерновой", "Белый", "Ржаной"], numbered=True)
print()
print("Выберите наполнитель. ", end="")
filler = pyinputplus.inputMenu(["Курица", "Индейка", "Ветчина", "Тофу"], numbered=True)
print()
print("Добавить сыр? (yes/no) ", end="")
cheese = pyinputplus.inputYesNo()
cheese = "С сыром" if cheese == "yes" else "Без сыра"
if cheese == "С сыром":
    print()
    print("Выберите тип сыра. ", end="")
    type_of_cheese = pyinputplus.inputMenu(["Чеддер", "Швейцарский", "Моцарелла"], numbered=True)
print()
print("Добавить майонез, горчицу, салат или помидор? (yes/no) ", end="")
add = pyinputplus.inputYesNo()
add = "добавить" if add == "yes" else "не добавлять"
if add == "добавить":
    print()
    print("Выберите что добавить? ", end="")
    what_add = pyinputplus.inputMenu(["Майонез", "Горчица", "Салат", "Помидор"], numbered=True)
print()
answer = "Количество бутербродов: "
quantity = pyinputplus.inputInt(prompt=answer, greaterThan=0)
print()
print(bread)
print(filler)
if cheese == "С сыром":
    print(f"С сыром {type_of_cheese}.")
if add == "добавить":
    print(f"Добавить {what_add}.")
print(f"Количество: {quantity}.")