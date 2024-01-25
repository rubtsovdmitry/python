import random, shutil, sys, time, bext


class Duckling:
    """создадим в конструкторе рандомного утёнка"""
    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])                                                   # в какую сторону смотрит утёнок
        self.body = random.choice([CHUBBY, VERY_CHUBBY])                                                # утёнок кругленький или нет
        self.mouth = random.choice([OPEN, CLOSED])                                                      # открытый клюв или нет
        self.wing = random.choice([OUT, UP, DOWN])                                                      # положение крыльев

        if self.body == CHUBBY:                                                                         # У круглых утят могут быть только глаза-бусинки
            self.eyes = BEADY
        else:                                                                                           # У очень круглых утят будут другие глаза
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD       

    def getHeadStr(self):
        """метод возвращает строковое значение с головой утёнка"""
        headStr = ''
        if self.direction == LEFT:                                                                      # ориентация налево
            """рот"""
            if self.mouth == OPEN:                                                                      # рот открыт
                headStr += '>'
            elif self.mouth == CLOSED:                                                                  # или рот закрыт
                headStr += '='

            """глаза"""
            if self.eyes == BEADY and self.body == CHUBBY:                                              # если глаза бусинки и тело круглое
                headStr += '"'  
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:                                       # если глаза бусинки и тело очень круглое
                headStr += '" '
            elif self.eyes == WIDE:                                                                     # просто широкие глаза
                headStr += "''"
            elif self.eyes == HAPPY:                                                                    # просто счастливые глаза 
                headStr += '^^'
            elif self.eyes == ALOOF:                                                                    # отчужденные глаза 
                headStr += '``'

            """затылок"""
            headStr += ') '                                             

        if self.direction == RIGHT:                                                                     # ориентация направо
            """затылок"""
            headStr += ' ('

            """глаза"""
            if self.eyes == BEADY and self.body == CHUBBY:                                              # если глаза бусинки и тело круглое
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:                                       # если глаза бусинки и тело очень круглое
                headStr += ' "'
            elif self.eyes == WIDE:                                                                     # просто широкие глаза
                headStr += "''"
            elif self.eyes == HAPPY:                                                                    # просто счастливые глаза 
                headStr += '^^'
            elif self.eyes == ALOOF:                                                                    # отчужденные глаза 
                headStr += '``'

            """рот"""
            if self.mouth == OPEN:                                                                      # рот открыт
                headStr += '<'
            elif self.mouth == CLOSED:                                                                  # или рот закрыт
                headStr += '='

        if self.body == CHUBBY:                                                                         # если тело просто круглое добавить пробел
            headStr += ' '

        return headStr                                                                                  # готовая голова утёнка

    def getBodyStr(self):
        """метод возвращает строковое значение с телом утёнка"""
        bodyStr = '('                                                                                   # левая часть тела
        if self.direction == LEFT:                                                                      # ориентация налево
            """размер тела"""
            if self.body == CHUBBY:                                                                     # тело круглое
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:                                                              # тело очень круглое
                bodyStr += '  '

            """крылья"""
            if self.wing == OUT:                                                                        
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:                                                                     # ориентация направо
            """крылья"""
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            """размер тела"""
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'                                                                                  # правая часть тела

        if self.body == CHUBBY:                                                                         # если тело просто круглое добавить пробел
            bodyStr += ' '

        return bodyStr                                                                                  # готовое тело утёнка

    def getFeetStr(self):
        """метод возвращает строковое значение с лапами утёнка"""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """метод последовательности отрисовки утёнка"""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()


def main():
    bext.clear()
    bext.fg("red")
    print('Нажмите Ctrl-C для выхода...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)                                                  # определим какое количество уток поместится в окне терминала (это количество элементов списка)

    while True:  
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            if (ducklingObj == None and random.random() <= DENSITY):
                    ducklingObj = Duckling()                                                            # создаётся объект "утёнок", при подходящих условиях
                    ducklingLanes[laneNum] = ducklingObj                                                # в список, вместо None, помещается объект "утёнок"

            if ducklingObj != None:
                print(ducklingObj.getNextBodyPart(), end='')
                if ducklingObj.partToDisplayNext == None:                                               # если дошла печать до ног, то изменяем объект "утёнок" в списке на None
                    ducklingLanes[laneNum] = None
            else:                
                print(' ' * DUCKLING_WIDTH, end='')
        print()  
        time.sleep(PAUSE)


# ввод констант
PAUSE = 0.2  
DENSITY = 0.10 

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0]                                                                   # получить ширину текущего терминала

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()