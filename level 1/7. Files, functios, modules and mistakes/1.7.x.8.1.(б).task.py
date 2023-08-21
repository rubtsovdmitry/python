def temperature_c_function(farenheit):
    temperature_c = (farenheit - 32) * 5 / 9
    return temperature_c


def temperature_k_function(temperature_c):
    temperature_k = temperature_c + 273.15    
    return temperature_k
farenheit = float(input("Введите температуру в фаренгейтах: "))


temperature_c = temperature_c_function(farenheit)
temperature_k = temperature_k_function(temperature_c)

print("Температура в цельсиях равна", round(temperature_c, 2))
print("Температура в кельвинах равна", round(temperature_k, 2))