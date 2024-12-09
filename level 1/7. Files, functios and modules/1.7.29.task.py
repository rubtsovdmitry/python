import random 

def my():
    x = random.randint(33, 126)
    return chr(x)


password_len = random.randint(7, 10)
password = ""
while password_len != 0:
    password += my()
    password_len -= 1

print("%35s" % "Генератор паролей:", password)