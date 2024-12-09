"""Руссифицированная часть модуля pyinputplus.
Только функция inputInt(). 
Здесь работают именованные аргументы только из списка: min, max, greaterThan, lessThan, limit и timeout 
(можно расширить функционал и для других функций и аргументов)."""


import time


def inputInt(prompt=str(), min=-1000_000_000, max=1000_000_000, greaterThan=-1000_000_000, lessThan=1000_000_000, limit=1000_000_000, timeout=1000_000_000):
    if prompt:
        pass
    else:
        prompt = "Введите целое число: "
    seconds, seconds2 = time.time(), time.time()
    while True and limit != 0 and (seconds2 - seconds) <= timeout:
        seconds2 = time.time()
        limit -= 1
        try:
            x = input(prompt)
            x = int(x)
            if x < greaterThan or x < min:
                print("Ошибка. Вы ввели слишком маленькое число.")
                if limit == 0:
                    print("Попытки ввода исчерпаны.")
                continue
            if x > lessThan or x > max:
                print("Ошибка. Вы ввели слишком большое число.")
                if limit == 0:
                    print("Попытки ввода исчерпаны.")
                continue
        except:
            print("Ошибка. Вы ввели не тот формат.")
            if limit == 0:
                    print("Попытки ввода исчерпаны.")
            continue
        else:            
            return x
    if (seconds2 - seconds) > timeout:
        print("Время ввода истекло.")
        return None
        
if __name__ == '__main__':
    pass
else:
    inputInt()