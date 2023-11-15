def my_def(number):
    if number[0:3].isdigit() and number[4:7].isdigit() and number[8:12].isdigit() and number[3] == "-" and number[7] == "-": 
        return True    
    else:
        return False
    

text = "Позвони мне завтра по номеру 415-555-1011. 415-555-9999 - это номер телефона моего офиса."

for i in range(len(text) - 12):
    number = text[i:(i + 12)]
    if my_def(number):
        print("%99s" % number)