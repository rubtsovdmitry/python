seconds = int(input("Введите количество секунд: "))

sec_in_min = 60
min_in_hour = 60
hour_in_day = 24

sec_in_hour = sec_in_min * min_in_hour
sec_in_day = sec_in_hour * hour_in_day

day = seconds // sec_in_day                                                     # производим целочисленное деление, чтобы узнать сколько целых дней
hour = (seconds % sec_in_day) // sec_in_hour                                    # узнаём остаток от деления на количество секунд в сутках, а затем производим целочисленное деление, чтобы узнать сколько целых часов
min = ((seconds % sec_in_day) % sec_in_hour) // sec_in_min                      # по аналогии узнаём сколько целых минут
sec = seconds % sec_in_min                                                      # а вот с секундами гораздо проще

print("Дней:", day, "*** часов:", hour, "*** минут:", min, "*** секунд:", sec)	