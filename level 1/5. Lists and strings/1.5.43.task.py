# ввод данных
while True:
    digit = input("%100s" % "Введите целое число, до которого будем искать все простые числа: ")
    try:
        digit = int(digit)
        break
    except:
        print("%99s" % "Вы ввели не число.")

# составим список, в котором будем искать простые числа
result_list = []
for i in range(1, digit + 1):
    result_list.append(i)
result_list.remove(1)

count = 0
p = 2
while True:
    
    for i in result_list:
        if i != p and i % p == 0:
            result_list.remove(i) 
    while True:
        p += 1
        if p in result_list:
            break        
    if p == result_list[-1]:    
        break
   
print(result_list)