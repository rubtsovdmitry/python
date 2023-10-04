# проверка ввода
while True:
    digit = input("%50s" % "Введите число в десятичной системе счисления: ")
    if digit.isdigit():
        break
digit = int(digit)
result = str()

while digit >= 1:
    remains = digit % 2
    result += str(remains)
    digit = int(digit / 2)
result = result[::-1]

print("%49s" % result)