def my_f(my_list):
     my_list.remove(min(my_list))
     my_list.remove(max(my_list))
     return sorted(my_list)

my_list = []
while True:
    digit = input("%100s" % "Введите число (чтобы прекратить введите \"Enter\"): ")
    try:
        if len(digit) > 0:
              digit = float(digit)
              my_list.append(digit)        
        elif len(digit) == 0 and len(my_list) < 4:             
             print("%99s" % "Вы патаетесь отменить ввод, когда список не достиг 4 значений.")             
        elif len(digit) == 0 and len(my_list) >= 4:             
             break                  
    except:
        print("%99s" % "Вы ввели не число.")

print("%99s" % my_f(my_list))