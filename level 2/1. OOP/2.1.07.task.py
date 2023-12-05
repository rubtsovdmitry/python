class User:
    count = 0                                               # создадим атрибут класса - счётчик регистраций
    def __init__(self, name, login, password):              # создаём атрибуты объекта
        self.__name = name
        self.__login = login
        self.__password = password
        User.count += 1                                     # прибавляет +1 к каждой регистрации

    def __repr__(self):
        return f"Имя: {self.__name}. Логин: {self.__login}."
    
    def get_name(self):                                     # создадим geter и seter для инкапсулированного атрибута self.__name
        return self.__name
    def set_name(self, value):
        self.__name = value
    name = property(get_name, set_name)
    
    def get_login(self):                                    # создадим geter и seter для инкапсулированного атрибута self.__login
        return self.__login
    def set_login(self, value):                             # выдаст исключение, если произойдёт попытка изменения login, так лучше, чем просто не делать seter
        raise AttributeError("Нельзя менять значение!")
    login = property(get_login, set_login)

    def get_password(self):                                 # создадим geter и seter для инкапсулированного атрибута self.__password
        return "***********"
    def set_password(self, value):                         
        self.__password = value
    password = property(get_password, set_password)

    def show_info(self):                                    # создадим метод показывающий состояние атрибутов объекта (имени и логина)
        print(f"Name: {self.__name}")
        print(f"Login: {self.__login}")

class SuperUser(User):                                      # создадим класс-наследник
    count = 0                                               # по анологии создадим атрибут для класса-наследника - счётчик регистраций
    def __init__(self, name, login, password, role):        # создаём атрибуты объекта класса-наследника путём наследования части их от родителя
        super().__init__(name, login, password)
        self.__role = role        
        SuperUser.count += 1                                # прибавляет +1 к каждой регистрации
        User.count -= 1                                     # нужно обязательно отнять 1 у суперкласса, т.к. наше обращение прибавило там единицу, и super() здесь не сработает, поэтому обращаемся в атрибуту супер-класса напрямую
    
    def __repr__(self):                          
        s = super().__repr__()
        return f"{s} Роль: {self.__role}."

    @property                                               # создадим geter и seter для инкапсулированного атрибута self.__role с помощью декораторов
    def role(self):
        return self.__role
    @role.setter
    def role(self, value):
        self.__role = value

    def show_info(self):                                    # создадим метод показывающий состояние атрибутов объекта (имени и логина, которых наследует + нового атрибута role)
        super().show_info()
        print(f"Role: {self.__role}")

################### тест ##############################################################################

user1 = User("Paul McCartney", "paul", "1234")       
user2 = User("George Harrison", "george", "5678")
user3 = User("Ringo Starr", "ringo", "qwerty")
admin = SuperUser("John Lennon", "john", "password", "admin")

print()
print(f"{user1}\n{user2}\n{user3}\n{admin}\n")
print(f"Обычных пользователей: {User.count}. Админов: {SuperUser.count}.\n")