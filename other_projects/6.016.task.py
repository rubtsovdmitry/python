import random, shutil, sys, time, bext

"""КОНСТАНТЫ"""
MIN_STREAM_LENGTH = 7
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']

DENSITY = 0.02                                                                                       # плотность

WIDTH = shutil.get_terminal_size()[0]                                                                # размер окна терминала

bext.clear()
bext.fg("green")
print('Нажмите <Ctrl-C> для выхода.')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:                                                      
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()  