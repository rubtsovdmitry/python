items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    }
]

brand = set()                       # заведём множество, в кот. будем помещать название брендов (оно само уберёт повторы)
for i in items:                     # обойдём в цикле все значения списка items
    brand.add(i.get("brand"))       # значения списка items являются словарями, обратимся по ключу "brand" к словарю и поместим значение, т.е. название бренда в множество, кот. будет нашим результатом
print(brand)