table = {
    "Звонки": 50,
    "Сообщения": 50
}

FIX_PRICE = 15.00
MINUTE_PRICE = 0.25
SMS_PRICE = 0.15
CALL_911_PRICE = 0.44
TAX = 5
minutes = int(input("%50s" % "Введите количество израсходованных минут: " ))
sms = int(input("%50s" % "Введите количество сообщений: "))
print()

if minutes <= table["Звонки"] and sms <= table["Сообщения"]:
    uplimit = 0
    tax_amount = (FIX_PRICE + CALL_911_PRICE) * (TAX / 100)
    amount_with_tax = FIX_PRICE + CALL_911_PRICE + tax_amount
elif minutes > table["Звонки"] and sms > table["Сообщения"]:
    uplimit = (minutes - table["Звонки"]) * MINUTE_PRICE + (sms - table["Сообщения"]) * SMS_PRICE
    tax_amount = (FIX_PRICE + CALL_911_PRICE + uplimit) * (TAX / 100)
    amount_with_tax = FIX_PRICE + CALL_911_PRICE + uplimit + tax_amount
elif minutes > table["Звонки"] and sms <= table["Сообщения"]:
    uplimit = (minutes - table["Звонки"]) * MINUTE_PRICE
    tax_amount = (FIX_PRICE + CALL_911_PRICE + uplimit) * (TAX / 100)
    amount_with_tax = FIX_PRICE + CALL_911_PRICE + uplimit + tax_amount
elif minutes <= table["Звонки"] and sms > table["Сообщения"]:
    uplimit = (sms - table["Сообщения"]) * SMS_PRICE
    tax_amount = (FIX_PRICE + CALL_911_PRICE + uplimit) * (TAX / 100)
    amount_with_tax = FIX_PRICE + CALL_911_PRICE + uplimit + tax_amount

print("%49s" % "Базовая сумма тарификации:", "%20s" % round(FIX_PRICE, 2), "$")
print("%49s" % "Сумма сверх лимита:", "%20s" % round(uplimit, 2), "$")
print("%49s" % "Сумма отчислений Call-центрам 911:", "%20s" % round(CALL_911_PRICE, 2), "$")
print("%49s" % "Сумма налога:", "%20s" % round(tax_amount, 2), "$")
print("%49s" % "Сумма к оплате:", "%20s" % round(amount_with_tax, 2), "$")