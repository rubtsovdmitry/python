amount = 0
for i in range(1,1000):
    if ((i % 3) == 0) or ((i % 5) == 0):
        amount += i
        print("%20s%20i%20s%20i" % ("Новая цифра", i, "Накопленная сумма", amount))
print("########################################################################################\n")
print("%60s%20i" % ("Сумма", amount))