print("Введите рост в американском стиле.")
height_f = int(input("Футы: "))
height_i = int(input("Дюймы: "))

f = 30.48
i = 2.54

height = height_f * f + height_i * i
height_m = int(height // 100)		    			# программа вычисляет сколько целых метров в росте
height_sm = int(height % 100 + 0.5)			        # программа вычисляет сколько см в остатке, 0.5 - нужно для правильного округления, т.к. int просто отбрасывает дробную часть

print()
print("Рост в метрической системе исчисления равен", height_m, "м", height_sm, "см")	