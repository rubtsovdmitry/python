my_list = []
while True:
     word = input("%100s" % "Введите слово (для отмены просто введите \"Enter\"): ")
     if word == "":
          break
     my_list.append(word)

result_list = []
for i in my_list:
     if i not in result_list:
          result_list.append(i)

print()
for i in result_list:
     print("%99s" % i)