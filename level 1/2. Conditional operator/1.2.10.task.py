print("%70s" % "Ноты:", "%20s" % "C, D, E, F, G, A, B.")
print("%70s" % "Октавы:", "%20s" % "0, 1, 2, 3, 4, 5, 6, 7, 8.")
note = input("%71s" % "Введите ноту и октаву (к примеру: C4 или B8): ")

C4 = 261.63; D4 = 293.66; E4 = 329.63; F4 = 349.23; G4 = 392.00; A4 = 440.00; B4 = 493.88           # можно записывать строки через ";", но лучше так не делать. Здесь очень подходящий случай.
base_digit = "4"                                                                                    # введена 4 для точки отсчёта
octave = "012345678"                                                                                # октава может находится только среди этих чисел

try:
    if note[0] == "C" and len(note) == 2 and note[-1] in octave:                                    # условие, при кот. проверяется существование ноты, октавы, и длины ноты не более 2-х знаков. Если условие не будет выполнено, то не будет создана переменная для расчёта.
        base = C4
    elif note[0] == "D" and len(note) == 2 and note[-1] in octave:
        base = D4
    elif note[0] == "E" and len(note) == 2 and note[-1] in octave:
        base = E4
    elif note[0] == "F" and len(note) == 2 and note[-1] in octave:
        base = F4
    elif note[0] == "G" and len(note) == 2 and note[-1] in octave:
        base = G4
    elif note[0] == "A" and len(note) == 2 and note[-1] in octave:
        base = A4
    elif note[0] == "B" and len(note) == 2 and note[-1] in octave:
        base = B4

    if note[-1] == base_digit:
        mgz = base
    elif note[-1] < base_digit:
        base_digit = int(base_digit)
        digit = int(note[-1])
        while digit != base_digit:
            base_digit -= 1
            base /= 2
        mgz = base
    elif note[-1] > base_digit:
        base_digit = int(base_digit)
        digit = int(note[-1])
        while digit != base_digit:
            base_digit += 1
            base *= 2
        mgz = base
    print("%70s" % "Частота ноты:", round(mgz, 2))
except:
    print("%70s" % "Была допущена ошибка в вводе.")