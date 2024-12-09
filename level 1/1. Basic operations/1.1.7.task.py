seconds = int(input("Введите количество секунд: "))

sec_in_min = 60
min_in_hour = 60
hour_in_day = 24

seconds_plus = 2.5 * sec_in_min * min_in_hour                                                    # здесь, согласно новым условиям прибавляем 2,5 часа
sec_in_hour = sec_in_min * min_in_hour
sec_in_day = sec_in_hour * hour_in_day

day = (seconds + seconds_plus) // sec_in_day                                                     # производим целочисленное деление, чтобы узнать сколько целых дней
hour = ((seconds + seconds_plus) % sec_in_day) // sec_in_hour                                    # узнаём остаток от деления на количество секунд в суиках, а затем производим целочисленное деление, чтобы узнать сколько целых часов
min = (((seconds + seconds_plus) % sec_in_day) % sec_in_hour) // sec_in_min                      # по аналогии узнаём сколько целых минут
sec = (seconds + seconds_plus) % sec_in_min                                                      # а вот с секундами гораздо проще

print("Дней:", day, "*** часов:", hour, "*** минут:", min, "*** секунд:", sec)