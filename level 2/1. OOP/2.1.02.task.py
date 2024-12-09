class User:
    def __init__(self, floor=1):                                        # гарантировано создадим атрибуты __state и __floor для объекта
        self.__state = "идём пешком"                                    # состояние по-умолчанию для атрибута __state - это "идём пешком"
        self.__floor = floor                                            # состояние по-умолчанию для атрибута __floor, если не указан другой - это первый этаж
    
    def get_state(self):                                                # создаём geter для состояния объекта
        return self.__state
    state = property(get_state)

    def get_floor(self):                                                # создаём geter для состояния объекта
        return self.__floor
    def set_floor(self, floor):                                         # создаём seter для состояния объекта
        self.__floor = floor
    floor = property(get_floor, set_floor)

    def __repr__(self):                                                 # функционал печати
        if self.__state == "едем на лифте":
            return f"Человек приехал на лифте на {self.__floor} этаж."                   
        else:
            return f"Человек пришёл пешком на {self.__floor} этаж."

    def elevator(self):
        if self.__state == "идём пешком":                               # если self.__state = "идём пешком", то запустится 
            self.__state = "едем на лифте"            
        
    def on_foot(self):
        if self.__state == "едем на лифте":                             # если self.__state = "едем на лифте", то запустится 
            self.__state = "идём пешком"
            

human = User()                                                          # создаём объект, который по-умолчанию находится на первом этаже
human.floor = 3                                                         # меняем этаж на третий
print(f"Человек {human.state} на {human.floor} этаж.")                  # используем в печати geter-ы из класса