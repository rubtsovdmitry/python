import re

"""КЛАСС СТЕК"""
class Stack:
    def __init__(self):
        self.__data = list()                                                                            # для стека выбран список 

    def push(self, item):                                                                               # добавить элемент в очередь
        self.__data.append(item)                                            

    def pop(self):                                                                                      # убрать последний элемент
        if len(self.__data) > 0:                                            
            return self.__data.pop()                                            
        return None                                                                                     # вернуть None, если стек пуст

    def peek(self):                                                                                     # посмотреть вершину стека
        if len(self.__data) > 0:                                            
            return self.__data[-1]                                          
        return None                                                                                     # вернуть None, если стек пуст    

    def is_empty(self):                                                                                 # проверить пуст ли стек
        return len(self.__data) == 0                                                                    

    def size(self):                                                                                     # узнать размер стека
        return len(self.__data)                                     

    def show(self):                                                                                     # вывести стек в stdout    
        print("\nСтек:")
        print("\n".join([str(i) for i in self.__data[::-1]]), "\n")


# входные данные
a = open("./4.37.class_stack_tags.html", "r")                                                           # передаётся файл, в котором будем производить поиск
s = a.read()
my_search_list = [re.compile(r"<head[^<]*>|</head>"), re.compile(r"<title[^<]*>|</title>")]             # задаётся шаблон для поиска

# составим список списков, в каждом подсписке только один тип тегов, к примеру [['<head>', '</head>'], ['<title>', '</title>']]
result = []
for i in my_search_list:
    x = i.findall(s)
    result.append(x)

# основной цикл
finish_text = ""    
for a in result:
    # для head
    temp = Stack()
    for b in a:
        if "<head" in b:
            temp.push(b)
        elif "</head>" in b:
            if temp.size() < 1:
                print("Неудача с </head>.")
                print("Закрывающих тегов </head> больше, чем нужно.")
                finish_text = "Тест не пройден!"
            else:
                temp.pop()
    if temp.size() > 0:
        print("Открывающих тегов <head> больше, чем нужно.")
        temp.show()
        finish_text = "Тест не пройден!"

    # для title
    temp = Stack()
    for b in a:
        if "<title" in b:
            temp.push(b)
        elif "</title>" in b:
            if temp.size() < 1:
                print("Неудача с </title>.")
                print("Закрывающих тегов </title> больше, чем нужно.")
                finish_text = "Тест не пройден!"
            else:
                temp.pop()
    if temp.size() > 0:
        print("Открывающих тегов <title> больше, чем нужно.")
        temp.show()
        finish_text = "Тест не пройден!"

if finish_text:
    print(finish_text)    
else:
    print("Тест пройден!")