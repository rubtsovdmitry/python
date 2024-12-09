price = float(input("%50s" % "Введите сумму покупки в рублях в формате 00.00: "))
score = float(input("%50s" % "Введите сколько денег внесено в рублях в формате 00.00: "))
price_kop = int(price * 100)                                                                    # переведём рубли в копейки, сменим тип на int (необязательно)
score_kop = int(score * 100)                                                                    # переведём рубли в копейки, сменим тип на int (необязательно)

NOMINAL_5000r_in_kop = 500000
NOMINAL_1000r_in_kop = 100000
NOMINAL_500r_in_kop = 50000
NOMINAL_200r_in_kop = 20000
NOMINAL_100r_in_kop = 10000
NOMINAL_50r_in_kop = 5000
NOMINAL_10r_in_kop = 1000
NOMINAL_5r_in_kop = 500
NOMINAL_2r_in_kop = 200
NOMINAL_1r_in_kop = 100
NOMINAL_50kop = 50
NOMINAL_10kop = 10
NOMINAL_5kop = 5
NOMINAL_1kop = 1

sdacha_in_kop = score_kop - price_kop

# блок для купюр
sdacha_5000r = sdacha_in_kop // NOMINAL_5000r_in_kop
sdacha_1000r = (sdacha_in_kop - sdacha_5000r * NOMINAL_5000r_in_kop) // NOMINAL_1000r_in_kop
sdacha_500r = (sdacha_in_kop - sdacha_5000r * NOMINAL_5000r_in_kop - sdacha_1000r * NOMINAL_1000r_in_kop) // NOMINAL_500r_in_kop
sdacha_200r = (sdacha_in_kop - sdacha_5000r * NOMINAL_5000r_in_kop - sdacha_1000r * NOMINAL_1000r_in_kop - sdacha_500r * NOMINAL_500r_in_kop) // NOMINAL_200r_in_kop
sdacha_100r = (sdacha_in_kop - sdacha_5000r * NOMINAL_5000r_in_kop - sdacha_1000r * NOMINAL_1000r_in_kop - sdacha_500r * NOMINAL_500r_in_kop - sdacha_200r * NOMINAL_200r_in_kop) // NOMINAL_100r_in_kop
sdacha_50r = (sdacha_in_kop - sdacha_5000r * NOMINAL_5000r_in_kop - sdacha_1000r * NOMINAL_1000r_in_kop - sdacha_500r * NOMINAL_500r_in_kop - sdacha_200r * NOMINAL_200r_in_kop - sdacha_100r * NOMINAL_100r_in_kop) // NOMINAL_50r_in_kop
sdacha_10r = (sdacha_in_kop - sdacha_5000r * NOMINAL_5000r_in_kop - sdacha_1000r * NOMINAL_1000r_in_kop - sdacha_500r * NOMINAL_500r_in_kop - sdacha_200r * NOMINAL_200r_in_kop - sdacha_100r * NOMINAL_100r_in_kop - sdacha_50r * NOMINAL_50r_in_kop) // NOMINAL_10r_in_kop

# блок для монет
sum_banknot_in_kop = (sdacha_in_kop - sdacha_5000r * NOMINAL_5000r_in_kop - sdacha_1000r * NOMINAL_1000r_in_kop - sdacha_500r * NOMINAL_500r_in_kop - sdacha_200r * NOMINAL_200r_in_kop - sdacha_100r * NOMINAL_100r_in_kop - sdacha_50r * NOMINAL_50r_in_kop - sdacha_10r * NOMINAL_10r_in_kop)
sdacha_5r = sum_banknot_in_kop // NOMINAL_5r_in_kop
sdacha_2r = (sum_banknot_in_kop - sdacha_5r * NOMINAL_5r_in_kop) // NOMINAL_2r_in_kop
sdacha_1r = (sum_banknot_in_kop - sdacha_5r * NOMINAL_5r_in_kop - sdacha_2r * NOMINAL_2r_in_kop) // NOMINAL_1r_in_kop
sdacha_50k = (sum_banknot_in_kop - sdacha_5r * NOMINAL_5r_in_kop - sdacha_2r * NOMINAL_2r_in_kop - sdacha_1r * NOMINAL_1r_in_kop) // NOMINAL_50kop
sdacha_10k = (sum_banknot_in_kop - sdacha_5r * NOMINAL_5r_in_kop - sdacha_2r * NOMINAL_2r_in_kop - sdacha_1r * NOMINAL_1r_in_kop - sdacha_50k * NOMINAL_50kop) // NOMINAL_10kop
sdacha_5k = (sum_banknot_in_kop - sdacha_5r * NOMINAL_5r_in_kop - sdacha_2r * NOMINAL_2r_in_kop - sdacha_1r * NOMINAL_1r_in_kop - sdacha_50k * NOMINAL_50kop - sdacha_10k * NOMINAL_10kop) // NOMINAL_5kop
sdacha_1k = (sum_banknot_in_kop - sdacha_5r * NOMINAL_5r_in_kop - sdacha_2r * NOMINAL_2r_in_kop - sdacha_1r * NOMINAL_1r_in_kop - sdacha_50k * NOMINAL_50kop - sdacha_10k * NOMINAL_10kop - sdacha_5k * NOMINAL_5kop) // NOMINAL_1kop

print()
print("%49s" % "Сдача")
print("%49s" % "Купюра 5000р. (количество):", sdacha_5000r)
print("%49s" % "Купюра 1000р. (количество):", sdacha_1000r)
print("%49s" % "Купюра 500р. (количество):", sdacha_500r)
print("%49s" % "Купюра 200р. (количество):", sdacha_200r)
print("%49s" % "Купюра 100р. (количество):", sdacha_100r)
print("%49s" % "Купюра 50р. (количество):", sdacha_50r)
print("%49s" % "Купюра 10р. (количество):", sdacha_10r)
print("%49s" % "Монета 5р. (количество):", sdacha_5r)
print("%49s" % "Монета 2р. (количество):", sdacha_2r)
print("%49s" % "Монета 1р. (количество):", sdacha_1r)
print("%49s" % "Монета 50коп. (количество):", sdacha_50k)
print("%49s" % "Монета 10коп. (количество):", sdacha_10k)
print("%49s" % "Монета 5коп. (количество):", sdacha_5k)
print("%49s" % "Монета 1коп. (количество):", sdacha_1k)