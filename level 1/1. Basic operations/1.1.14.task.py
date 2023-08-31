KM_IN_MILE = 1.609
L_IN_GALLON = 3.785
mile_gallon = float(input("%50s" % "Введите потребление топлива в милях на галлон: "))
l_100km = 1 / (mile_gallon * KM_IN_MILE / L_IN_GALLON) * 100
print("%49s" %  "Потребление топлива в литрах на 100 км:", "%.2f" % l_100km)