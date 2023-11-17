import re

def my_def(i):
    return [x for x in i if x != ""][0]


buf = open("./osnovy_informatiki.txt", "r")
s = buf.read()

regex_obj = re.compile(r"""https://w?w?w?\.?(\S*\.\S{2,3})/ 
                       | http://w?w?w?\.?(\S*\.\S{2,3})/""", re.VERBOSE)
x =regex_obj.findall(s)
x = [my_def(i) for i in x]

print()
for i in x:
    print("%33s" % i)
print()