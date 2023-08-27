import time                                                                                                                              

def my_function_pi(tochnost):
    v_skobkax = 1
    first_3 = 3
    first_5 = 5
    while first_3 <= tochnost or first_5 <= tochnost:
        v_skobkax = v_skobkax - 1 / first_3 + 1 / first_5
        first_3 += 4
        first_5 += 4
    digit_pi = 4 * v_skobkax
    return digit_pi

    
print()
tochnost = input("Введите максимальное число в знаменателе слагаемых и вычитаемых чисел (этим мы определим точность расчёта) ")
try:
    tochnost = int(tochnost)
    print(f"Максимальное число точности: {tochnost:,}")
    t1 = time.time()
    digit_pi = my_function_pi(tochnost)
    t2 = time.time()
    print("Число ПИ равно:", digit_pi)
    print("Время на вычисление в секундах равно", (t2 - t1))
except:
    print("Вы ввели не число")