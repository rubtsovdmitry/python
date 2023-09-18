A = 0
B = 1
MAX = 4000000
amount_total = 0

while (A + B) < MAX:
    amount = A + B
    A = amount
    if (A < MAX) and (A % 2) == 0:
        amount_total += A
        print(A, "Чётное")
    elif (A < MAX) and (A % 2) != 0:
        print(A)

    amount = A + B
    B = amount
    if (B < MAX) and (B % 2) == 0:
        amount_total += B
        print(B, "Чётное")
    elif (B < MAX) and (B % 2) != 0:
        print(B)
print("#################################################\n")
print("Сумма всех чётных элементов =", amount_total)