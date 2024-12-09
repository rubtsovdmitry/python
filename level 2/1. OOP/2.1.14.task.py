class Inventory():                                                          
    """Это класс для инвентаря героя игры"""

    HORIZONTAL = "ABCDEFGHI"                                                                                  # это ячейки по горизонтали для инвентаря
    VERTICAL = "123456789"                                                                                    # это ячейки по вертикали для инвентаря
    SIZE = 5                                                                                                  # размер инвентаря по-умолчанию

    @classmethod                                                                                              # этот метод класса нужен для генерации начального инвентаря
    def __make_field(cls):
        inventory = []
        for a, b in zip(cls.HORIZONTAL, range(cls.SIZE)):            
            inventory.append([])
            for c, d in zip(cls.VERTICAL, range(cls.SIZE)):
                inventory[b].append({(a + c): "⬜"})
        return inventory
                                 
    def __init__(self):
        self._inventory = self.__class__.__make_field()                                                       # инвентарь генерируется атоматически при создании и будет определённого размера

    def get_inventory(self):                                                                                  # getter для инвенторя. инвентарь - это список списков, в которых находятся словари
        return self._inventory                                                                                # Вид: [[{'A1': ' '}, {'A2': ' '}, {'A3': ' '}, {'A4': ' '}, {'A5': ' '}], [{'B1': ' '}, {'B2': ' '}, {'B3': ' '}, {'B4': ' '}, {'B5': ' '}], [{'C1': ' '}, {'C2': ' '}, {'C3': ' '}, {'C4': ' '}, {'C5': ' '}], [{'D1': ' '}, {'D2': ' '}, {'D3': ' '}, {'D4': ' '}, {'D5': ' '}], [{'E1': ' '}, {'E2': ' '}, {'E3': ' '}, {'E4': ' '}, {'E5': ' '}]]
    inventory = property(get_inventory)

    def interactive_inventory(self):                                                                          # показать инвентарь интерактивно
        print()
        print(" ", end="")
        for a, b in zip(self.__class__.VERTICAL, range(len(self._inventory))):
            print(a, end=" ")                         
        for a, a2 in zip(self._inventory, self.__class__.HORIZONTAL):
            print()                        
            print(a2, end="")
            for b in a:                                
                for c in b.values():
                    print(c, end="")
        print("\n")

    def mod_inventory_plus_one(self):                                                                         # прокачать инвентарь, если это возможно (максимальный размер 10)
        if len(self._inventory) == 9:
            print("Инвентарь достиг максимального размера.")
        else:
            new_size = len(self._inventory) + 1
            for i in range(len(self._inventory)):
                self._inventory[i].append({(self.__class__.HORIZONTAL[i])\
                +(self.__class__.VERTICAL[new_size - 1]): "⬜"})
            self._inventory.append([])
            for a, b in zip(self.__class__.VERTICAL, range(new_size)):
                self._inventory[(new_size - 1)].append({(self.__class__.HORIZONTAL[new_size-1] + a): "⬜"})

    def mod_inventory_put_in(self, number):                                                                   # заполнить инвентарь (работает только для одной ячейки)           
        for index, item in enumerate(self._inventory):
            for index_2, item_2 in enumerate(item):
                if number in item_2:                                        
                    self._inventory[index][index_2] = {number: "⬛"}

    def mod_inventory_put_out(self, number):                                                                  # убрать элемент из инвентаря (работает только для одной ячейки)           
        for index, item in enumerate(self._inventory):
            for index_2, item_2 in enumerate(item):
                if number in item_2:                                        
                    self._inventory[index][index_2] = {number: "⬜"}           
        

a = Inventory()                                                                                               # создадим инвентарь, который будет со значениями по-умолчанию
a.mod_inventory_put_in("A1")                                                                                  # положим объект в ячейку
a.mod_inventory_plus_one()                                                                                    # вызовем метод прокачки инвентаря
a.interactive_inventory()                                                                                     # метод выведет инвентарь интерактивно
print(a.inventory)                                                                                            # выведем состояние инвентаря через свойство (getter) в виде списка списков с вложенными словарями

a.mod_inventory_put_in("D4")
a.mod_inventory_plus_one()  
a.interactive_inventory()   
print(a.inventory)          

a.mod_inventory_put_in("G6")
a.mod_inventory_plus_one()  
a.interactive_inventory()   
print(a.inventory)          

a.mod_inventory_put_in("G8")
a.mod_inventory_plus_one()  
a.interactive_inventory()   
print(a.inventory)          

a.mod_inventory_plus_one()                                                                                    # при очередной попытке апгрейда инвентаря выйдет сообщение, что Инвентарь достиг максимального размера.
a.mod_inventory_put_out("A1")                                                                                 # уберём объект из ячейку
a.interactive_inventory()   