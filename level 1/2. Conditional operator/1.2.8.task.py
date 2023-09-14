level_of_noise = int(input("%100s" % "Введите уровень шума в децибелах: "))

jackhammer = 130
lawn_mower = 106
alarm_clock = 70
silent_room = 40

if level_of_noise == jackhammer:
    print("%99s" % "Уровень шума точно совпадает с уровнем отбойного молотка.")
elif level_of_noise == lawn_mower:
    print("%99s" % "Уровень шума точно совпадает с уровнем газовой газонокосилки.")
elif level_of_noise == alarm_clock:
    print("%99s" % "Уровень шума точно совпадает с уровнем будильника.")
elif level_of_noise == silent_room:
    print("%99s" % "Уровень шума точно совпадает с уровнем тихой комнаты.")
elif level_of_noise < silent_room:
    print("%99s" % "Уровень шума ниже уровня тихой комнаты.")
elif level_of_noise > silent_room and level_of_noise < alarm_clock:
    print("%99s" % "Уровень шума выше уровня тихой комнаты и ниже уровня будильника.")
elif level_of_noise > alarm_clock and level_of_noise < lawn_mower:
    print("%99s" % "Уровень шума выше уровня будильника и ниже уровня газовой газонокосилки.")
elif level_of_noise > lawn_mower and level_of_noise < jackhammer:
    print("%99s" % "Уровень шума выше уровня газовой газонокосилки и ниже уровня отбойного молотка.")
else:
    print("%99s" % "Уровень шума выше уровня отбойного молотка.")