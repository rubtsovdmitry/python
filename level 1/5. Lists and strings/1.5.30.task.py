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

proposal = proposal.split(" ")
print(proposal)