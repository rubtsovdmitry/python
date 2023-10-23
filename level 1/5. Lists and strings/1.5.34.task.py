proposal = input("%100s" % "Введите предложение: ")
proposal = proposal.lower()
proposal = proposal.replace(".", "")
proposal = proposal.replace(",","")
proposal = proposal.replace("!","")
proposal = proposal.replace("?","")
proposal = proposal.replace("-","")
proposal = proposal.replace(" '","")
proposal = proposal.replace("' ","")
proposal = proposal.replace(":","")
proposal = proposal.replace(";","")
proposal = proposal.replace("\"","")
my_list = proposal.split(" ")   

glasnie = ["a", "e", "i", "o", "u"]
soglasnie = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
result = []
for i in my_list:
    if i[0] in glasnie:
        result.append(i + "way")
    else:
        temp = str()
        temp_result = str()
        flag = 0
        for x in i:            
            if x in soglasnie and flag == 0:
                temp += x
            elif x not in soglasnie and flag == 0:
                flag = 1
                temp_result += x
            else:
                temp_result +=x
        temp_result += (temp + "ay")                    
        result.append(temp_result)
result = " ".join(result)
print("%99s" % result)