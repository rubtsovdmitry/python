my_list = [["x", " ", " ", " ", " ", " ", " ", " ", " "],\
           ["x", "x", " ", " ", " ", " ", " ", " ", " "],\
           ["x", "x", "x", " ", " ", " ", " ", " ", " "],\
           ["x", "x", "x", "x", " ", " ", " ", " ", " "],\
           ["x", "x", "x", "x", "x", " ", " ", " ", " "],\
           ["x", "x", "x", "x", "x", "x", " ", " ", " "],\
           ["x", "x", "x", "x", "x", "x", "x", "x", "x"],\
           ["x", "x", "x", "x", "x", "x", " ", " ", " "],\
           ["x", "x", "x", "x", "x", " ", " ", " ", " "],\
           ["x", "x", "x", "x", " ", " ", " ", " ", " "],\
           ["x", "x", "x", " ", " ", " ", " ", " ", " "],\
           ["x", "x", " ", " ", " ", " ", " ", " ", " "],\
           ["x", " ", " ", " ", " ", " ", " ", " ", " "]]

for a in my_list:
    for b in a:
        print(b, end="")
    print()
print()
print()
print()

####################################

width = len(my_list)
height = len(my_list[0])
for a in range(height):
    for b in range(width):
        print(my_list[b][a], end="")
    print()
print()
print()
print()

####################################

my_list_2 = []
for a in my_list:
    my_list_2.append(a[::-1])

for a in my_list_2:
    for b in a:
        print(b, end="")
    print()
print()
print()
print()

####################################

width = len(my_list_2)
height = len(my_list_2[0])
for a in range(height):
    for b in range(width):
        print(my_list_2[b][a], end="")
    print()
print()
print()
print()