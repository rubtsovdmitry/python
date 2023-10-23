proposal = input("%50s" % "Введите предложение: ")
print()

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
proposal = proposal.lower()

proposal = proposal.split(" ")
if proposal == proposal[::-1]:
    print("%50s" % "Предложение является словесным палинромом.")
else:
    print("%50s" % "Предложение не является словесным палинромом.")