"""КЛАСС ОЧЕРЕДЬ-FIFO"""
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
    

# создать объект класса "Stack"
a = Queue()                                                 

# добавляем или убираем элементы из очереди FIFO
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.enqueue(6)
a.enqueue(7)
a.enqueue(8)
a.enqueue(9)
a.dequeue()

# посмотрим последний элемент в очереди
print("\nПоследний в очереди:", a.rear())

# посмотрим первый элемент в очереди
print("\nПервый в очереди:", a.front())

# проверить пуста ли очередь
print("\nПуста ли очередь?", a.is_empty())

# узнать размер очереди
print("\nРазмер очереди:", a.size())

# вывести очередь
a.show()

# очистить очередь и вывести
a.clear(); a.show()