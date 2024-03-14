"""КЛАСС СТЕК"""
class Stack:
    def __init__(self):
        self.__data = list()                                            # для стека выбран список 

    def push(self, item):                                               # добавить элемент в очередь
        self.__data.append(item)            

    def pop(self):                                                      # убрать последний элемент
        if len(self.__data) > 0:            
            return self.__data.pop()            
        return None                                                     # вернуть None, если стек пуст

    def peek(self):                                                     # посмотреть вершину стека
        if len(self.__data) > 0:            
            return self.__data[-1]          
        return None                                                     # вернуть None, если стек пуст    

    def is_empty(self):                                                 # проверить пуст ли стек
        return len(self.__data) == 0                                    

    def size(self):                                                     # узнать размер стека
        return len(self.__data)     

    def show(self):                                                     # вывести стек в stdout    
        print("\nСтек:")
        print("\n".join([str(i) for i in self.__data[::-1]]), "\n")
    

# создать объект класса "Stack"
a = Stack()                                                 

# добавляем или убираем элементы из очереди LIFO
a.push(1)
a.push(10)
a.push(100)
a.push(2)
a.pop()

# посмотрим вершину стека
print("\nВершина стека:", a.peek())

# проверить пуст ли стек
print("\nПуст ли стек?", a.is_empty())

# узнать размер стека
print("\nРазмер стека:", a.size())

# вывести стек
a.show()