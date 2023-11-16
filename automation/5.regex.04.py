import re
   
buf = open("./Аякc-Софокл.txt", "r")
s = buf.read()

regex_obj = re.compile(r"\sАякс")                   # составим регулярное выражение для поиска имени Аяск
s = regex_obj.sub(" Иван", s) 
regex_obj = re.compile(r"«Аякс")                    # составим регулярное выражение для поиска имени Аяск
s = regex_obj.sub(" «Иван", s)
regex_obj = re.compile(r"\(Аякс")                   # составим регулярное выражение для поиска имени Аяск
s = regex_obj.sub(" (Иван", s) 

buf_2 = open("./Аякc-Софокл_mod.txt", "w")
buf_2.write(s)
buf_2.close()