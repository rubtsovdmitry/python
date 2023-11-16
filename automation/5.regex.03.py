import re
   
buf = open("./Посылки.txt", "r")
s = buf.read()

regex_obj = re.compile(r"\s(\d+\.\d{2})")                   # составим регулярное выражение для поиска сумм
x = regex_obj.findall(s)                                    # список сумм
x = sum([float(i) for i in x])

print()
print(f"Сумма всех посылок: {(x):.2f}")
print()