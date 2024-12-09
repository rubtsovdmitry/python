import re

buf = open("./Список кредитных карт.txt", "r")
s = buf.read()

regex_obj = re.compile(r"\d{4} \d{4} \d{4} \d{4} ?\d?")                   
s = regex_obj.sub("<credit card> **************", s)
regex_obj = re.compile(r"\d{16}(\d{3})?")                   
s = regex_obj.sub("<credit card> **************", s)

print(s)