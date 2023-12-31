def result(data, search):    
    if len(data) == 0:                            # базовый случай, будем уменьшать строку до пустой
        return 0
    mod = data[1:len(data)]                       # вот здесь происходит уменьшение строки <mod>
    if search == data[0]:
        return 1 + result(mod, search)            # а теперь передаём уменьшенную строку в рекурсию <mod>
    else: 
        return result(mod, search)                # и здесь передаём уменьшенную строку в рекурсию <mod>


data = "Рекурсивные алгоритмы применимы в большом количестве задач, определения которых могут быть выражены через самих себя. \
И список подобных задач не ограничивается работой с целыми числами. \
Представьте, что вам необходимо выяснить, сколько раз определенный символ встречается в строке. \
Для решения этой задачи может быть написана рекурсивная функция, принимающая на вход строку и искомый символ и возвращающая количество появлений этого символа в строке."
search = "а"

print(result(data, search))