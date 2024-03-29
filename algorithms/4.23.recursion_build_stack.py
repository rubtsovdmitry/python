def main(a):
    if len(a) == 1:                                                 # базовый случай
        count = 0                                                   # счётчик
        print(f"{a}, вершина стека")                                # вернёт список [[1], 0], в котором первый элемент - это верхний элемент стека, а второй - счётчик
        return [a, count]
    else:
        temp = a[-1:]                                               # перед тем как отправить переменную в рекурсию, запомним срез, включающий последний элемент
        a.pop()                                                     # модернизируем переменную перед отправкой в рекурсию
        rec = main(a)                                               # из рекурсии возвращается [[1], 0] -> [[1, 2], -1] -> [[1, 2, 3], -2] ... и т.д.
        count = rec[-1] - 1                                         # с каждым возвратом от базового случая счётчик уменьшается на 1
        result = rec[0] + temp                                      # собирает разобранный список (двумерный массив) обратно
        for_print = []                                              
        for_print.append(result[-1])                                # достаём из собираемого списка последний элемент и отображаем его в виде [1], [2] или [n]
        print(f"{for_print}, уровень {count}.")
        return [result, count]

a = [1,2,3,4,5,6,7,8,9,10]
print("--------------------------------------------\n", main(a))