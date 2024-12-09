holidays = {
    "Happy new year": "1 january",
    "Day of Canada": "1 july",
    "Christmas": "25 december"
}

month = input("%100s" % "Введите месяц по-английски полностью (к примеру: january или february): ")
day = input("%100s" % "Введите день месяца (к примеру: 1 или 10): ")

plus = day + " " + month

test = True
for holiday, date in zip(holidays.keys(), holidays.values()):                                       # функция zip обходит в цикле параллельно сразу два значения и может обатиться к любому из них, так и к другому за один проход
    if plus in date:
        print("%99s" % "На данную дату попадает праздник:", holiday)
        test = False    
if test:
    print("%99s" % "На данную дату не приходятся праздники.")