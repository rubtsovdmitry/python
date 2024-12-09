from math import inf


def function_node(costs):
    lowest_cost = inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:                                                                            # обязательно берём минимальную цену, т.к. неизвестная цена всегда бесконечность
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node                                                                                                         # функция вернёт узел с минимальной ценой из ХЕШ-ТАБЛИЦЫ ДЛЯ ХРАНЕНИЯ СТОИМОСТИ ВСЕХ УЗЛОВ


#############################################################################
#############################################################################
"""СОЗДАНИЕ ГРАФА С ИСПОЛЬЗОВАНИЕМ ХЕШ-ТАБЛИЦЫ. ВХОДНЫЕ ДАННЫЕ."""
graph = {}                                                                                                                          # словарь соседей со стоимостями перехода ---> {'Начало': {'А': 5, 'Б': 2}, 'А': {'В': 4, 'Г': 2}, 'Б': {'А': 8, 'Г': 7}, 'В': {'Г': 6, 'КОНЕЦ': 3}, 'Г': {'КОНЕЦ': 1}, 'КОНЕЦ': {}}

# начало                                                                                    
graph["Начало"] = {}                                                                                    
graph["Начало"]["А"] = 5
graph["Начало"]["Б"] = 2                                                                                    

# А                                                                                 
graph["А"] = {}
graph["А"]["В"] = 4
graph["А"]["Г"] = 2

# Б                                                                                 
graph["Б"] = {}                                                                                 
graph["Б"]["А"] = 8                                                                                 
graph["Б"]["Г"] = 7 

# В 
graph["В"] = {}                                                                                 
graph["В"]["Г"] = 6
graph["В"]["КОНЕЦ"] = 3

# Г 
graph["Г"] = {}                                                                                 
graph["Г"]["КОНЕЦ"] = 1

# КОНЕЦ                                                                                 
graph["КОНЕЦ"] = {}                                                                                                                 # у конечного узла нет соседей
#############################################################################
#############################################################################
"""ХЕШ-ТАБЛИЦА ДЛЯ ХРАНЕНИЯ СТОИМОСТИ ВСЕХ УЗЛОВ. ЗАПОЛНЯЕТСЯ В ПРОЦЕССЕ."""                                                     
costs = {}                                                                                                                          # ---> {'А': 5, 'Б': 2, 'В': inf, 'Г': inf, 'КОНЕЦ': inf}
costs["А"] = 5
costs["Б"] = 2
costs["В"] = inf                                                                                                                    # пока это бесконечность                                                                            
costs["Г"] = inf                                                                                                                    # пока это бесконечность                                                                                           
costs["КОНЕЦ"] = inf                                                                                                                # пока это бесконечность                                                                            
#############################################################################
#############################################################################
"""ХЕШ-ТАБЛИЦА ДЛЯ РОДИТЕЛЕЙ. ЗАПОЛНЯЕТСЯ В ПРОЦЕССЕ."""                                                                                 
parents = {}                                                                                                                        # ---> {'А': 'Начало', 'Б': 'Начало', 'В': None, 'Г': None, 'КОНЕЦ': None}
parents["А"] = "Начало"                         
parents["Б"] = "Начало"                         
parents["В"] = None
parents["Г"] = None
parents["КОНЕЦ"] = None                         
#############################################################################
#############################################################################
"""СПИСОК ДЛЯ ОТСЛЕЖИВАНИЯ ВСЕХ УЖЕ ОБРАБОТАННЫХ УЗЛОВ. НУЖЕН ДЛЯ ИЗБЕЖАНИЯ ЦИКЛОВ."""                           
processed = []                          

node = function_node(costs)                                                                                                        # найдём узел с наименьшей стоимостью из уже известных и необработанных ---> к примеру: Б
while node is not None:                                                                                                            # цикл завершится, если обработаны все узлы
    cost = costs[node]                                                                                                             # ---> int; цена для узла, он же узел с наименьшей стоимостью
    neighbors = graph[node]                                                                                                        # ---> 'Б': {'А': 8, 'Г': 7}; соседи узла
    for n in neighbors.keys():                                                                                                     # переберём всех соседей текущего узла
        new_cost = cost + neighbors[n]                                                                                             # цена для соседа текущего узла
        if costs[n] > new_cost:                                                                                                    # проверка цены в хеш-таблице
            costs[n] = new_cost                                                                                                    # обновим, если новая цена меньше той, что в хеш-таблице
            parents[n] = node                                                                                                      # обновим родителя, если новая цена меньше той, что в хеш-таблице
    processed.append(node)                                                                                                         # помещаем узел в список обработанных узлов
    node = function_node(costs)                                                                                                    # найдём узел с наименьшей стоимостью из уже известных и необработанных

print()
print("Словарь с наименьшими ценами для узлов", costs)
print()
print("Словарь с родителями для узлов", parents)
print()