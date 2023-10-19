def my_cook_measure(cups, tablespoons, teaspoons):
    tablespoons_in_cup = 16
    teaspoons_in_tablespoons = 3
    teaspoons_in_cups = teaspoons_in_tablespoons * tablespoons_in_cup
    
    teaspoons = teaspoons + teaspoons_in_tablespoons * tablespoons + teaspoons_in_cups * cups

    cups_result = teaspoons // teaspoons_in_cups
    tablespoons_result = (teaspoons - cups_result * teaspoons_in_cups) // teaspoons_in_tablespoons
    teaspoons_result = (teaspoons - cups_result * teaspoons_in_cups - tablespoons_result * teaspoons_in_tablespoons)    
    return (cups_result, tablespoons_result, teaspoons_result)


while True:
    cups = input("%50s" % "Введите количество стаканов: ")
    tablespoons = input("%50s" % "Введите количество столовых ложек: ")
    teaspoons = input("%50s" % "Введите количество чайных ложек: ")
    print()
    try:
        cups = int(cups)
        tablespoons = int(tablespoons)
        teaspoons = int(teaspoons)
        if cups < 0 or tablespoons < 0 or teaspoons < 0:
            print(("%49s" % "Вы ввели отрицательные значения."))
            continue
        break
    except:
        print("%49s" % "Вы допустили ошибку при вводе.")

result = my_cook_measure(cups, tablespoons, teaspoons)

print("%49s" % f"Количество чашек: {result[0]}", "%49s" % f"Количество столовых ложек: {result[1]}", "%49s" % f"Количество чайных ложек: {result[2]}")