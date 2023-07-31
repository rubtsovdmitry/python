# первый вариант (лучший)
print("Первый вариант")
print()
for i in range(0, 7):
    print(10 ** i)
print()


# второй вариант
print("Второй вариант")
print()
a = str()
b = "1000000"
for i in b:
    a += i
    print(a)
print()


# третий вариант
print("Третий вариант")
print()
first_digit = 10
count = 0
while count <= 6:
    print(first_digit ** count)
    count += 1
print()

# четвёртый вариант
print("Четвёртый вариант")
print()
first_digit = "1"
count = 6
while count >= 0:
    print(first_digit)
    first_digit += "0"
    count -= 1