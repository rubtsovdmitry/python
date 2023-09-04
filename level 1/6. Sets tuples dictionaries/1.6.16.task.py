receipt = {
    'Наименование': ['HORTEX Фасоль стручк. б/зам', 'Яблоки КРИПС ПИНК отборные', 'ДОБ.НЕК.БОД.ЦИТ.ап/гр/ман/ли', 'СВЯТ.ИСТ.Вода прир.пит.негаз. ПЭТ 5л', 'СПк Свинина с грибами зап. 1к', 'МЯГК ВАФ С ВАР СГ ЯШ', 'КАРТОФЕЛЬ БЕЛЫЙ РАНН', 'ЧУДО Мол.ВАН.стер.фр.2% 200г', 'Пакет майка', 'GOUR.Корм MON PETIT.кош.кур.', 'Ф-Н.Пюре и/яб/абр со сл/сах', 'MATTI Мюсли ОРЕХ/ЯБЛОКО 250г', 'ХЛ.ДОМ Кекс Яг. Лук.нач.ч.см', 'GREENF.Чай GOLD.CEYL.чер.', 'Куриное Филе ПЕТЕЛ.на подл'],
    'Кол-во': [1, 0.466, 2, 1, 0.178, 2, 0.57, 5, 1, 10, 6, 1, 1, 1, 0.758],
    'Цена': [124.9, 129.9, 189.9, 104.9, 699.0, 37.6, 44.9, 44.9, 6.9, 23.9, 57.9, 129.9, 89.9, 119.9, 355.01],
    'Цена со скидкой': [124.9, 129.9, 109.9, 104.9, 699.0, 37.6, 44.9, 44.9, 6.9, 17.9, 34.9, 69.9, 59.9, 69.9, 279.89],
}

# здесь мы обходим в цикле, с использованием функции zip два списка из аргументов для ключей основного словаря
# в итоге расчитывается цена товарной корзины без скидки
amount = 0
for i, i2 in zip(receipt["Кол-во"], receipt["Цена"]):
    amount += i * i2

# здесь мы обходим в цикле, с использованием функции zip два списка из аргументов для ключей основного словаря (аналогия предыдущему блоку, но с другими данными)
# в итоге расчитывается цена товарной корзины со скидкой
amount_discont = 0
for i, i2 in zip(receipt["Кол-во"], receipt["Цена со скидкой"]):
    amount_discont += i * i2

print("Цена без скидки", round(amount, 2))
print("Цена со скидкой", round(amount_discont, 2))
print("Сумма скидки", round((amount - amount_discont), 2))