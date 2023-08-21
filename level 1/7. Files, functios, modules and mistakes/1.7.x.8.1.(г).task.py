def perevod(sm):
    FOOT = 30.48
    INCH = 2.54
    foot = int(sm // FOOT)
    inch = int((sm % FOOT) / INCH + 0.5)
    return (foot, inch)


sm = float(input("Введите количество сантиметров для перевода в футы и дюймы: "))
foot_and_inch = perevod(sm)

print(foot_and_inch)