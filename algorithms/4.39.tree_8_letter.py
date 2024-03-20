#################################################################################################################################
# Первый вариант, найти все имена длиною в восемь символов и поместить их в отдельный список.
#################################################################################################################################

"""ФУНКЦИЯ ДЛЯ ПОИСКА ИМЕНИ С ПОДХОДЯЩЕЙ ДЛИНОЙ."""
def main(node):
    print("Текущий узел:", node["name"], end="   ")
    if len(node["name"]) == 8:
        result.append(node["name"])
        print("Найдено подходящее имя:", node["name"], end=" ")    
    print("\n")
    if len(node["children"]) > 0:                                                            # рекурсивный случай
        for child in node["children"]:
            main(child)

"""СОЗДАНИЕ СТРУКТУРЫ ДАННЫХ ДЛЯ ДЕРЕВА."""
# здесь описаны все узлы
root = { "name": "Alice", "children": [] }
node2 = { "name": "Bob", "children": [] }
node3 = { "name": "Caroline", "children": [] }
node4 = { "name": "Darya", "children": [] }
node5 = { "name": "Eve", "children": [] }
node6 = { "name": "Fred", "children": [] }
node7 = { "name": "Gonzalo", "children": [] }
node8 = { "name": "Hadassah", "children": [] }
# здесь описаны, только те узлы, у которых есть дети. По-другому, те узлы, которые не будут являться базовыми случаями (листьями дерева).
root["children"] = [node2, node3]
node2["children"] = [node4]
node3["children"] = [node5, node6]
node5["children"] = [node7, node8]
# print(root) --> {'name': 'Alice', 'children': [{'name': 'Bob', 'children': [{'name': 'Darya', 'children': []}]}, {'name': 'Caroline', 'children': [{'name': 'Eve', 'children': [{'name': 'Gonzalo', 'children': []}, {'name': 'Hadassah', 'children': []}]}, {'name': 'Fred', 'children': []}]}]}

"""КОД"""
print()
result = []
main(root)
print("Список с именами:", result, "\n")
print("###############################################################################################")

#################################################################################################################################
# Второй вариант, найти любое имя длиною в восемь символов и показать его.
#################################################################################################################################

"""ФУНКЦИЯ ДЛЯ ПОИСКА ИМЕНИ С ПОДХОДЯЩЕЙ ДЛИНОЙ."""
def main(node):
    print("Текущий узел:", node["name"])
    print(f"Проверка: подходит ли текущий узел {node["name"]} условиям поиска?\n---------------------------------------------")
    if len(node["name"]) == 8:
        return node["name"]                                                                  # Базовый случай, при котором поиск прекращается
    elif len(node["children"]) > 0:                                                          # рекурсивный случай
        for child in node["children"]:
            temp = main(child)
            if temp is not None:                                                             # очень важная запись, при использовании прямого обхода базовый случай также достигается, когда доходит до последнего листа дерева, который может уже вернуть None (этот возврат нужно игнорировать)
                return temp


"""СОЗДАНИЕ СТРУКТУРЫ ДАННЫХ ДЛЯ ДЕРЕВА."""
# здесь описаны все узлы
root = { "name": "Alice", "children": [] }
node2 = { "name": "Bob", "children": [] }
node3 = { "name": "Caroline", "children": [] }
node4 = { "name": "Darya", "children": [] }
node5 = { "name": "Eve", "children": [] }
node6 = { "name": "Fred", "children": [] }
node7 = { "name": "Gonzalo", "children": [] }
node8 = { "name": "Hadassah", "children": [] }
# здесь описаны, только те узлы, у которых есть дети. По-другому, те узлы, которые не будут являться базовыми случаями (листьями дерева).
root["children"] = [node2, node3]
node2["children"] = [node4]
node3["children"] = [node5, node6]
node5["children"] = [node7, node8]
# print(root) --> {'name': 'Alice', 'children': [{'name': 'Bob', 'children': [{'name': 'Darya', 'children': []}]}, {'name': 'Caroline', 'children': [{'name': 'Eve', 'children': [{'name': 'Gonzalo', 'children': []}, {'name': 'Hadassah', 'children': []}]}, {'name': 'Fred', 'children': []}]}]}

"""КОД"""
print()
print("Нашли:", main(root), "\n")