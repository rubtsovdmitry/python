# ввод данных
nums = ['+7 (960) 870-22-29', '+7 (926) 184-98-14', '+7 (960) 750-30-94', '+7 (926) 302-98-89', '+7 (916) 634-55-56', '+7 (960) 814-20-17', '+7 (960) 438-13-75', '+7 (926) 184-98-14', '+7 (960) 616-92-88', '+7 (999) 325-03-31', '+7 (495) 804-89-53', '+7 (926) 184-98-14', '+7 (916) 950-04-91', '+7 (960) 616-92-88', '+7 (960) 616-92-88', '+7 (999) 325-03-31', '+7 (915) 478-27-38', '+7 (916) 254-83-22', '+7 (495) 704-04-87', '+7 (960) 750-30-94', '+7 (499) 148-33-29', '+7 (916) 634-55-56', '+7 (926) 184-98-14', '+7 (900) 045-24-15', '+7 (900) 922-37-25', '+7 (960) 814-20-17', '+7 (495) 804-89-53', '+7 (960) 870-22-29', '+7 (960) 616-92-88', '+7 (960) 750-30-94', '+7 (499) 932-24-07', '+7 (999) 325-03-31', '+7 (916) 634-55-56', '+7 (960) 750-30-94', '+7 (960) 870-22-29', '+7 (960) 750-30-94', '+7 (960) 870-22-29', '+7 (915) 478-27-38', '+7 (960) 616-92-88', '+7 (916) 254-83-22', '+7 (999) 872-70-56', '+7 (926) 184-98-14', '+7 (495) 804-89-53', '+7 (495) 804-89-53', '+7 (495) 804-89-53', '+7 (960) 616-92-88', '+7 (926) 208-72-22', '+7 (900) 922-37-25', '+7 (916) 950-04-91', '+7 (915) 478-27-38', '+7 (926) 208-72-22', '+7 (960) 911-09-70', '+7 (926) 208-72-22', '+7 (999) 325-03-31', '+7 (499) 163-06-85', '+7 (915) 478-27-38', '+7 (926) 302-98-89', '+7 (999) 325-03-31', '+7 (960) 870-22-29', '+7 (916) 950-04-91', '+7 (916) 634-55-56', '+7 (916) 254-83-22', '+7 (900) 335-38-27', '+7 (900) 045-24-15', '+7 (900) 481-88-07', '+7 (999) 325-03-31', '+7 (915) 478-27-38', '+7 (499) 163-06-85', '+7 (960) 870-22-29', '+7 (926) 897-30-99', '+7 (900) 045-24-15', '+7 (916) 950-04-91', '+7 (926) 302-98-89', '+7 (926) 302-98-89', '+7 (900) 481-88-07', '+7 (495) 704-04-87', '+7 (499) 163-06-85', '+7 (495) 804-89-53', '+7 (960) 870-22-29', '+7 (960) 750-30-94', '+7 (900) 922-37-25', '+7 (916) 254-83-22', '+7 (495) 704-04-87', '+7 (960) 814-20-17', '+7 (916) 950-04-91', '+7 (916) 254-83-22', '+7 (960) 750-30-94', '+7 (916) 634-55-56', '+7 (495) 704-04-87', '+7 (999) 325-03-31', '+7 (495) 804-89-53', '+7 (915) 949-38-81', '+7 (926) 208-72-22', '+7 (499) 163-06-85', '+7 (916) 634-55-56', '+7 (916) 634-55-56', '+7 (960) 911-09-70', '+7 (999) 951-31-21', '+7 (900) 481-88-07', '+7 (499) 148-33-29', '+7 (900) 922-37-25', '+7 (926) 208-72-22', '+7 (900) 045-24-15', '+7 (495) 804-89-53', '+7 (916) 634-55-56', '+7 (960) 616-92-88', '+7 (960) 750-30-94', '+7 (916) 634-55-56', '+7 (499) 163-06-85', '+7 (916) 950-04-91', '+7 (915) 949-38-81', '+7 (960) 870-22-29', '+7 (900) 335-38-27', '+7 (960) 870-22-29', '+7 (926) 184-98-14', '+7 (900) 045-24-15', '+7 (915) 478-27-38', '+7 (926) 184-98-14', '+7 (900) 045-24-15', '+7 (900) 045-24-15', '+7 (960) 870-22-29', '+7 (495) 804-89-53', '+7 (900) 045-24-15', '+7 (915) 949-38-81', '+7 (916) 950-04-91', '+7 (960) 870-22-29', '+7 (999) 325-03-31', '+7 (916) 634-55-56', '+7 (499) 163-06-85', '+7 (960) 814-20-17', '+7 (499) 148-33-29', '+7 (999) 872-70-56', '+7 (999) 325-03-31', '+7 (900) 922-37-25', '+7 (960) 616-92-88', '+7 (900) 922-37-25', '+7 (900) 045-24-15', '+7 (916) 634-55-56', '+7 (900) 045-24-15', '+7 (900) 045-24-15', '+7 (999) 872-70-56', '+7 (960) 750-30-94', '+7 (900) 922-37-25', '+7 (960) 911-09-70', '+7 (999) 951-31-21', '+7 (926) 184-98-14', '+7 (900) 922-37-25', '+7 (960) 616-92-88', '+7 (499) 163-06-85', '+7 (495) 804-89-53', '+7 (926) 184-98-14', '+7 (916) 950-04-91', '+7 (960) 870-22-29', '+7 (495) 804-89-53', '+7 (999) 325-03-31', '+7 (900) 045-24-15', '+7 (926) 208-72-22', '+7 (926) 302-98-89', '+7 (926) 302-98-89', '+7 (900) 922-37-25', '+7 (960) 870-22-29', '+7 (900) 481-88-07', '+7 (900) 045-24-15', '+7 (916) 950-04-91', '+7 (960) 750-30-94', '+7 (960) 911-09-70', '+7 (499) 148-33-29', '+7 (960) 616-92-88', '+7 (926) 208-72-22', '+7 (499) 932-24-07', '+7 (916) 634-55-56', '+7 (916) 634-55-56', '+7 (926) 208-72-22', '+7 (900) 045-24-15', '+7 (926) 208-72-22', '+7 (960) 616-92-88', '+7 (495) 804-89-53', '+7 (495) 704-04-87', '+7 (960) 870-22-29', '+7 (499) 932-24-07', '+7 (960) 750-30-94', '+7 (999) 325-03-31', '+7 (900) 922-37-25', '+7 (999) 325-03-31', '+7 (900) 045-24-15', '+7 (960) 750-30-94', '+7 (926) 184-98-14', '+7 (960) 911-09-70', '+7 (916) 707-62-70', '+7 (926) 302-98-89', '+7 (960) 750-30-94', '+7 (900) 481-88-07', '+7 (926) 184-98-14', '+7 (900) 922-37-25', '+7 (495) 804-89-53', '+7 (960) 814-20-17', '+7 (900) 922-37-25', '+7 (926) 302-98-89', '+7 (499) 932-24-07', '+7 (499) 163-06-85']
nums2 = {499, 495, 916, 968, 888}

# преобразуем наши множества в множества со значениями одинакового типа 
nums = set(nums)  
nums2 = {str(i) for i in nums2}

nums3 = set()
for i in nums:
    if i[4:7] in nums2:
        nums3.add(i[4:7])
print(nums3, "Количество уникальных кодов городов, с которых звонили:", len(nums3))