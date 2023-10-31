# ввод данных
score = {
    1: "aeilnorstu",
    2: "dg",
    3: "bcmp",
    4: "fhvwy",
    5: "k",
    8: "jx",
    10: "qz"
}
text = input("%100s" % "Введите текст на английском языке: ")

result = int()
for i in text:
    for a, b in score.items():
        if i in b:
            result += a

print("%99s" % f"Количество очков: {result}.")