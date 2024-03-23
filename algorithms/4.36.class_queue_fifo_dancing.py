"""КЛАСС ОЧЕРЕДЬ-FIFO, который был описан в программе <<<Класс "Очередь-FIFO">>>."""
import copy


class Queue:
    def __init__(self):
        self.__data = list()                                            # для очереди выбран список 

    def enqueue(self, item):                                            # добавить элемент в очередь
        self.__data.append(item)            
    
    def dequeue(self):                                                  # убрать первый элемент
        if len(self.__data) > 0:            
            return self.__data.pop(0)            
        return None                                                     # вернуть None, если очередь пуста

    def rear(self):                                                     # посмотреть последний элемент в очереди
        if len(self.__data) > 0:            
            return self.__data[-1]          
        return None                                                     # вернуть None, если стек пуст    

    def front(self):                                                    # посмотреть первый элемент в очереди
        if len(self.__data) > 0:            
            return self.__data[0]          
        return None                                                     # вернуть None, если стек пуст    

    def is_empty(self):                                                 # проверить пуста ли очередь
        return len(self.__data) == 0                                    

    def size(self):                                                     # узнать размер очереди
        return len(self.__data)     

    def clear(self):                                                    # очистить очередь
        self.__data = []

    def show(self):                                                     # вывести очередь в stdout    
        if self.__data != []:
            print("\nОчередь:")
            result = "\n".join([str(i) for i in self.__data])
            result = result.removesuffix("\n")
            print(result)
        else:
            print("\nОчередь пуста.\n")
    
#######################################################################################################
########## ПЕРВЫЙ ВАРИАНТ (простой) ###################################################################
#######################################################################################################

print("\nПЕРВЫЙ ВАРИАНТ.\n")

# входные данные
data = [("Василий", "м"), ("Виталий", "м"), ("Виктор", "м"), ("Пётр", "м"), ("Евгений", "м"), ("Николай", "м"),\
        ("Ирина", "ж"), ("Екатерина", "ж"), ("Евгения", "ж"), ("Анастасия", "ж")]

# создадим 2 очереди
men = Queue()
women = Queue()

# разберём данные по очередям
while data != []:
    temp = data.pop(0)
    if temp[1] == "м":
        men.enqueue(temp[0])
    else:
        women.enqueue(temp[0])

# составим список танцоров
dance = []
while men.size() > 0 and women.size() > 0:
    dance.append((men.dequeue(), women.dequeue()))

# вывод 
dance = [" + ".join(i) for i in dance]
print("Пары танцоров:\n ", "\n  ".join(dance), "\n\n", "****************************")

#######################################################################################################
########## ВТОРОЙ ВАРИАНТ (сложный) ###################################################################
#######################################################################################################

print("\nВТОРОЙ ВАРИАНТ (сложный).\n")

# входные данные (сложный вариант, в котором каждый танцор имеет оценку)
data = [("Василий", "м", 3), ("Виталий", "м", 8), ("Виктор", "м", 7), ("Пётр", "м", 8), ("Евгений", "м", 5), ("Николай", "м", 9),\
        ("Ирина", "ж", 5), ("Екатерина", "ж", 9), ("Евгения", "ж", 9), ("Анастасия", "ж", 4)]

# модернизация входных данных (этот блок отсутствует в простом варианте)
eval = sorted([i[-1] for i in data], reverse=True)                                                                                      # --> [10, 9, 9, 9, 8, 8, 7, 5, 5, 4] - список оценок
temp_data = copy.copy(data)
data = []
for a in eval:
    for b in temp_data:
        if a in b:
            data.append(b)
            temp_data.remove(b)

# код ниже повторяет код из простого варианта, отличаться будет только результат обработки

# создадим 2 очереди
men = Queue()
women = Queue()

# разберём данные по очередям
while data != []:
    temp = data.pop(0)
    if temp[1] == "м":
        men.enqueue(temp[0])
    else:
        women.enqueue(temp[0])

# составим список танцоров
dance = []
while men.size() > 0 and women.size() > 0:
    dance.append((men.dequeue(), women.dequeue()))

# вывод 
dance = [" + ".join(i) for i in dance]
print("Пары танцоров:\n ", "\n  ".join(dance), "\n")