import pprint

def palindrome(i):
    if len(i) <= 1:                                                      
        return "Палиндром"
    elif i[0] != i[-1]:
        return "---"                                                           
    return palindrome(i[1:-1])    
    

data = {"казак", "шалаш", "потоп", "закат", "солнце", "река", "мадам"}
result = dict()
for i in data:
    result[i] = palindrome(i)

pprint.pprint(result)