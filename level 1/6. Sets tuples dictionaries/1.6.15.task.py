# первый способ
number = input("Введите номер банковской карты ")

if number[0] == "2":
    print("Мир")
elif number[0:2] == "30" or number[0:2] == "36" or number[0:2] == "38":
    print("Diners Club")
elif number[0:2] == "31" or number[0:2] == "35":
    print("JCB International")    
elif number[0:2] == "34" or number[0:2] == "37":
    print("American Express")
elif number[0] == "3":
    print("American Express, JCB International, Diners Club")
elif number[0] == "4":
    print("Visa")
elif number[0:2] == "50" or number[0:2] == "56" or number[0:2] == "57" or number[0:2] == "58":
    print("Maestro")    
elif number[0:2] == "51" or number[0:2] == "52" or number[0:2] == "53" or number[0:2] == "54" or number[0:2] == "55":
    print("MasterCard")
elif number[0] == "5":
    print("MasterCard, Maestro")
elif number[0:2] == "60":
    print("Discover")
elif number[0:2] == "62":
    print("China UnionPay")
elif number[0:2] == "63" or number[0:2] == "67":
    print("Maestro")
elif number[0] == "6":
    print("Maestro, China UnionPay, Discover")
elif number[0] == "7":
    print("УЭК")

##############################################

# второй способ
dict_pay_system = {
    "Мир": [2], 
    "American Express, JCB International, Diners Club": [3], 
    "Diners Club": [30, 36, 38], 
    "JCB International": [31, 35], 
    "American Express": [34, 37], 
    "VISA": [4], 
    "MasterCard, Maestro": [5], 
    "Maestro": [50, 56, 57, 58, 63, 67], 
    "MasterCard": [51, 52, 53, 54, 55], 
    "Maestro, China UnionPay, Discover": [6], 
    "Discover": [60], 
    "China UnionPay": [62],     
    "УЭК": [7]
}
number = input("Введите номер банковской карты ")

for x, y in dict_pay_system.items():
    if int(number[0:2]) in y:
        print(x)
    elif int(number[0]) in y:
        print("Входит в группу", x)