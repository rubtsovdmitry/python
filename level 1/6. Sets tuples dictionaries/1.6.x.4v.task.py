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

# в начале определим самую дорогую цену
expensive_price = 0
for i in items:
    expensive_price = i["price"] if i["price"] > expensive_price else expensive_price

# Теперь будем искать наименование товара и его бренд с самой дорогой ценой
result = list()
a = " "
for i in items:
    if i["price"] == expensive_price:
        result.append(i["name"] + " " + i["brand"] + " " + str(i["price"]))
print("Список товаров и их брендов с самой дорогой ценой:", result)