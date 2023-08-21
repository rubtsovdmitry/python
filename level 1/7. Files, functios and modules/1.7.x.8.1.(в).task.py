def sm_function(foot, inch):
    FOOT = 30.48
    INCH = 2.54
    sm = foot * FOOT + inch * INCH
    return sm


foot = float(input("%23s" % "Введите длину в футах: "))
inch = float(input("%23s" % "и дюймах: "))

sm = sm_function(foot, inch)
print("Перевод футов и дюймов в сантиметры равен: ", sm)