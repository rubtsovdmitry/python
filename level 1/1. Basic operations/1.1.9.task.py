ACREE = 43560
lenght = float(input("Введите длину садового участка в футах: "))
width = float(input("Введите ширину садового учасика в футах: "))
area = lenght * width
area_acree = area / ACREE
print("Площадь участка в акрах:", round(area_acree, 2))