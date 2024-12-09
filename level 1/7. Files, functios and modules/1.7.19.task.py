import my_lib


digits = range(1, 13)
lines = ("", "Two turtle doves,", "Three French hens,", "Four calling birds,", "Five golden rings", "Six geese-a-laying,", "Seven swans-a-swimming,", "Eight maids-a-milking,", "Nine drummers drumming,", "Ten pipers piping,", "Eleven ladies dancing,", "Twelve lords-a-leaping,")
count = 0
plus = str()
print()
for a, b in zip(digits, lines):
    if count == 0:
        print("On the", my_lib.my_function(a), "day of Christmas")        
        print("my true love sent to me:")        
        print("A partridge in a pear tree.")
        print()
    else:
        print("On the", my_lib.my_function(a), "day of Christmas")
        print("my true love sent to me:")
        plus = b + "\n" + plus       
        print(plus, end="")
        print("And a partridge in a pear tree.")
        print()
    count += 1