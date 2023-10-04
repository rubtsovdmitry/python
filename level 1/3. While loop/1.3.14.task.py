import random

count = 0
digit_max = 0
change_max_count = 0
while count < 100:
    count += 1
    digit_x = random.randint(1, 100)
    if digit_x > digit_max:
        digit_max = digit_x
        change_max_count += 1
        print("Счётчик:", "%5s" % count, "     новая цифра:", "%5s" % digit_x, "     - это новый максимум", "%5s" % change_max_count, "-я смена максимума")
    else:
        print("Счётчик:", "%5s" % count, "     новая цифра:", "%5s" % digit_x)