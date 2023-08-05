# 1-й способ

# ввод данных (без проверки входных данных)
digit = int(input("Введите число от 1 до 9: "))
print()

# решение
print("1")
count = 1
result = 1
while count < digit:
    count += 1
    result = result * 10 + count
    print(result)

#####################################3

# 2-й способ (через строки)

# ввод данных (без проверки входных данных)
digit = int(input("Введите число от 1 до 9: "))
print()

# решение
result = "1"
print(result)
count = 1
while count < digit:
    count += 1
    result += str(count)
    print(result)