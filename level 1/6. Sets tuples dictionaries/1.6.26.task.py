my_dict = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 1, "g": 1}
result = [i for i in my_dict if my_dict[i] == 1]
print(result)