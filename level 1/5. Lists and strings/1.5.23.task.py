my_list = []
while True:
    digit = input("%100s" % "Введите число для заполнения списка (для отмены просто нажмите <Enter>): ")
    if digit == "":
        break
    my_list.append(int(digit))
my_list.sort()
print("Числа в порядке возрастания: ", end="")
for i in my_list:
    print(i, " ", end="")
print()