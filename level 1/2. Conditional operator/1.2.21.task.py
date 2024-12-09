table = {
    0.0: "Низкий уровень",
    0.4: "Удовлетворительный уровень",
    0.6: "Высокий уровень",
}
estimation = float(input("%100s" % "Введите оценку с точностью, кроме максимальной (0.0, 0.4 или 0.6 и выше): "))
increase = 2400

if estimation not in table and estimation < 0.6:
    print("%99s" % "Вы ввели неверные данные")
elif estimation >= 0.6:
    print("%99s" % "Высокий уровень рейтинга. Прибавка составит:", (increase * 0.6), "долларов США.")
elif estimation in table:
    print("%98s" % str(table[estimation]) + ". Прибавка составит:", (increase * estimation), "долларов США.")