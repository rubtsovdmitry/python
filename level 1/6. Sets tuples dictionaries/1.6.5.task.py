days = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
money = 500

month = input("Введите название месяца: ")
print("Количество дней в месяце", days.get(month))                            # здесь идёт обращение к словарю явным образом, если month будет введён с ошибкой, то выведет тип данных None
print("Премия составит:", (days.get(month) * money), "руб.")        