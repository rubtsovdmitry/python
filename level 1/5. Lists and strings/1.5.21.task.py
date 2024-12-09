def my(things):
    result = str()
    for index, value in enumerate(things):
        if index != (len(things) - 1):
            result += (value + ", ")
        else:            
            result = result.removesuffix(", ")         
            result += (" and " + value + ".")
    temp = result[0]
    result = temp.upper() + result.removeprefix(temp)
    return result


things = ["spoon", "fork", "knife", "cup", "jug"]
result = my(things)
print(result)