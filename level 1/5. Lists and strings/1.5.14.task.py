# ввод данных
proposal = input("Введите текст: ")

# приведем текст в порядок, удалив из него лишнее и сделав одинаковый регистр
proposal = proposal.replace(" ", "")
proposal = proposal.replace("-", "")
proposal = proposal.replace("!", "")
proposal = proposal.replace(".", "")
proposal = proposal.lower()

print("Предложение палиндром") if proposal == proposal[::-1] else print("Предложение не палиндром")