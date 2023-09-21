import random

print("%60s" % "Игра: \"Камень, ножницы, бумага\".")

user_win = 0
user_loss = 0
user_ties = 0

while True:
    print()
    answer = input("%61s" % "Желаете сыграть? (да/нет): ")                            # если ответ "нет", то цикл сразу же закончится и программа завершится
    if answer == "нет":
        break
    elif answer != "да" and answer != "нет":                                 # если ответ не подходящий, то сразу перекинет в начало цикла
        continue
    else:                                                                    # игра запускается        
        x = random.randint(1,3)                                              # компьютер сгенерит значение (камень/ножницы/бумага)
        pc = "К" if x == 1 else ("Н" if x == 2 else "Б")
        print()
        print("%60s" % "Вам предстоит выбрать: камень(К)/ножницы(Н)/бумага(Б).")
        while True:
            user = input("%61s" % "Введите (К, Н или Б): ")
            if user == "К" or user == "Н" or user == "Б":                    # если ответ по выбору (камень/ножницы/бумага) не устроит вопрос в цикле повторится
                break            
        if pc == user:
            user_ties +=1
            result = "ничья"
        elif pc == "К" and user == "Б":
            user_win += 1
            result = "пользователь выигрывает"
        elif pc == "К" and user == "Н":
            user_loss += 1
            result = "пользователь проигрывает"
        elif pc == "Н" and user == "Б":
            user_loss += 1
            result = "пользователь проигрывает"
        elif pc == "Н" and user == "К":
            user_win += 1
            result = "пользователь выигрывает"
        elif pc == "Б" and user == "К":
            user_loss += 1
            result = "пользователь проигрывает"
        elif pc == "Б" and user == "Н":
            user_win += 1
            result = "пользователь выигрывает"
        print()
        print("%60s" % "Компьютер", pc)
        print("%60s" % "Пользователь", user)
        print("%60s" % result)

print()
print("%60s" % "ИТОГО:")
print()
print("%60s" % "Компьютер:", user_loss)
print("%60s" % "Пользователь:", user_win)
print("%60s" % "Ничья:", user_ties)