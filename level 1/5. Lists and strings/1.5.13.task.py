# первый способ
word = input("Введите слово: ")
drow = word[::-1]                                   # перевернём строковую переменную 

if word == drow:                                    
    print("Слово палиндром")
else:
    print("Слово не палиндром")
print()

################################

# второй способ (просто запись условия в одну строку)
word = input("Введите слово: ")
drow = word[::-1]                                                             # перевернём строковую переменную 
print("Слово палиндром") if word == drow else print("Слово не палиндром")     # с функцией print запись в одну строку работает, а с присваиванием переменной (str) нет