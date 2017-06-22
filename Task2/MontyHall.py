# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import random

# from log_api import log

'''
You can delete the function MontyHall and write
your MontyHall
'''


def MontyHall(Dselect, Dchange):
    Dcar = random.randint(1, 3)
    # hit at the first and not change the mind
    if Dcar == Dselect and Dchange == 0:
        return 1
    # not hit at the first and not change the mind
    elif Dcar != Dselect and Dchange == 0:
        return 0
    # hit at the first and change the mind
    elif Dcar == Dselect and Dchange == 1:
        return 0
    # not hit at the first and change the mind
    else:
        return 1


if __name__ == '__main__':
    # repeat 10000 times
    n = 10000

    # not sure whether to change the mind
    win = 0
    for i in range(n):
        Dselect = random.randint(1, 3)
        Dchange = random.randint(0, 1)
        win = win + MontyHall(Dselect, Dchange)
    # log(float(win) / float(n))
    print(float(win) / float(n))

    # be sure not to change the mind
    win = 0
    for i in range(n):
        Dselect = random.randint(1, 3)
        Dchange = 0
        win = win + MontyHall(Dselect, Dchange)
    # log(float(win) / float(n))
    print(float(win) / float(n))

    # be sure to change the mind
    win = 0
    for i in range(n):
        Dselect = random.randint(1, 3)
        Dchange = 1
        win = win + MontyHall(Dselect, Dchange)
    # log(float(win) / float(n))
    print(float(win) / float(n))
