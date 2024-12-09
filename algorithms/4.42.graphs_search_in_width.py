"""КЛАСС ОЧЕРЕДЬ-FIFO"""
class Queue:
    def __init__(self):
        # для построения очереди выбран список
        self.__data = list()   

    # добавить элемент в очередь
    def enqueue(self, item):  
        self.__data.append(item)            
    
    # убрать самый первый элемент
    def dequeue(self):  
        if len(self.__data) > 0:            
            return self.__data.pop(0)            
        return None  # вернуть None, если очередь пуста

    # посмотреть последний элемент в очереди
    def rear(self):  
        if len(self.__data) > 0:            
            return self.__data[-1]          
        return None  # вернуть None, если стек пуст    

    # посмотреть первый элемент в очереди
    def front(self):  
        if len(self.__data) > 0:            
            return self.__data[0]          
        return None  # вернуть None, если стек пуст    

    # проверить пуста ли очередь (True или False)
    def is_empty(self):  
        return len(self.__data) == 0                                    

    # узнать размер очереди
    def size(self):  
        return len(self.__data)     

    # очистить очередь
    def clear(self):  
        self.__data = []

    # вывести очередь в stdout    
    def show(self):  
        if self.__data != []:
            print("\nОчередь:")
            result = "\n".join([str(i) for i in self.__data])
            result = result.removesuffix("\n")
            print(result)
        else:
            print("\nОчередь пуста.\n")
    

# Ввод данных. Представлен граф с помощью хеш-таблицы (словаря).
a = {
    "Девочка": ["Вася", "Петя"],

    "Вася": ["Семён", "Татьяна"],
    "Петя": ["Снежана"],
    
    "Семён": [],
    "Татьяна": ["Галя"],
    "Снежана": ["Катя", "Женя"],

    "Галя": ["Игорь"],
    "Катя": ["Человек-паук"],
    "Женя": ["Джон"],

    "Игорь": ["Железный человек"], 

    "Железный человек": ["Человек-паук"]
}

# кого мы ищем?
X = "Человек-паук"

# создадим объект очереди FIFO и произведём его первоначальное заполнение
my_queue = Queue()
for i in a["Девочка"]:
    my_queue.enqueue(i)
del a["Девочка"]  # удалим текущего человека из хеш-таблицы, это нужно для того, чтобы остановить основной цикл далее в коде

"""ДАЛЕЕ СЛЕДУЕТ ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ"""
people_checked = []  # здесь хранится список уже проверенных людей
while True:  
    check = my_queue.dequeue()  # проверяемый объект в очереди - первый в очереди FIFO, который из очереди удаляется
    people_checked.append(check)  # пополним список проверенных людей
    if check == X:
        print()
        print(f"{X} найден!!! Список людей, которых пришлось проверить: {people_checked}.")
        print()
        break
    # подцикл для соседей текущего человека
    if check in a:
        for i in a[check]:
            if i in people_checked:  # ранее этот человек уже проверялся и его имени больше нет в хеш-таблице, т.к. он удалён от туда
                pass
            else:
                my_queue.enqueue(i)
        del a[check]
    # остановим основной цикл, если искомый человек не найден
    if len(a) == 0 and my_queue.is_empty:
        print()
        print(f"{X} не найден!!! Список людей, которых пришлось проверить: {people_checked}.")
        print()
        break