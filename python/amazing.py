#! env python

import os
import random


def concat(r, text):
    return r + text


def rnd(count):
    return random.randint(1, count + 1)


def make_entry_line(max_width, random_gate_pos, result):
    entry_line = result

    for i in range(1, max_width + 1):
        if i == random_gate_pos:
            entry_line = concat(entry_line, '+  ')
        else:
            entry_line = concat(entry_line, '+--')

    # 180
    return concat(entry_line, '+')


def add_header(s):
    s = concat(
        s,
        'Amazing - Copyright by Creative Computing, Morristown, NJ')
    return concat(s, '\n')


def choose_randomly(default, *targets):
    x = rnd(len(targets))
    if x > len(targets):
        return default
    return targets[x - 1]


def doit(max_width, max_height):

    target = 0
    result = ''

    result = add_header(result)

    h = max_width
    v = max_height
    if h == 1 or v == 1:
        return

    wArray = [[0 for x in range(v + 1)] for y in range(h + 1)]
    vArray = [[0 for x in range(v + 1)] for y in range(h + 1)]

    q = 0
    z = 0
    x = rnd(h)

    result = make_entry_line(h, x, result)
    result = concat(result, '\n')

    # 190
    c = 1
    wArray[x][1] = c
    c = c + 1

    # 200
    r = x
    s = 1

    start = 270
    end = -1

    target = start

    while target != -1:
        if target == 210:
            if r != h:
                r = r + 1
                target = 260
            else:
                if s != v:
                    r = 1
                    s = s + 1
                    target = 260
                else:
                    r = 1
                    s = 1
                    target = 260
        elif target == 260:
            if wArray[r][s] == 0:
                target = 210
            else:
                target = start
        elif target == start:
            if r - 1 == 0:
                target = 600
            else:
                if wArray[r - 1][s] != 0:
                    target = 600
                else:
                    if s - 1 == 0:
                        target = 430
                    else:
                        if wArray[r][s - 1] != 0:
                            target = 430
                        else:
                            if r == h:
                                target = 350
                            else:
                                if wArray[r + 1][s] != 0:
                                    target = 350
                                else:
                                    target = choose_randomly(
                                        350,
                                        940, 980, 1020)
        elif target == 350:
            if s != v:
                if wArray[r][s + 1] != 0:
                    target = 410
                else:
                    target = 390
            else:
                if z == 1:
                    target = 410
                else:
                    q = 1
                    target = 390
        elif target == 390:
            target = choose_randomly(
                410,
                940, 980, 1090
            )
        elif target == 410:
            target = choose_randomly(
                430,
                940, 980
            )
        elif target == 430:
            if r == h:
                target = 530
            else:
                if wArray[r + 1][s] != 0:
                    target = 530
                else:
                    if s != v:
                        if wArray[r][s + 1] != 0:
                            target = 510
                        else:
                            target = 500
                    else:
                        if z == 1:
                            target = 510
                        else:
                            q = 1
                            target = 500
        elif target == 500:
            target = choose_randomly(
                510,
                940, 1020, 1090
            )
        elif target == 510:
            target = choose_randomly(
                530,
                940, 1020
            )
        elif target == 530:
            if s != v:
                target = 560
            else:
                target = 540
        elif target == 540:
            if z == 1:
                target = 940
            else:
                q = 1
                target = 570
        elif target == 560:
            if wArray[r][s + 1] != 0:
                target = 940
            else:
                target = 570
        elif target == 570:
            target = choose_randomly(
                940,
                940, 1090
            )
        elif target == 600:
            if s - 1 == 0:
                target = 790
            else:
                if wArray[r][s - 1] != 0:
                    target = 790
                else:
                    if r == h:
                        target = 720
                    else:
                        if wArray[r + 1][s] != 0:
                            target = 720
                        else:
                            if s != v:
                                if wArray[r][s + 1] != 0:
                                    target = 700
                                else:
                                    target = 680
                            else:
                                if z == 1:
                                    target = 700
                                else:
                                    q = 1
                                    target = 680
        elif target == 680:
            target = choose_randomly(
                700,
                980, 1020, 1090
            )
        elif target == 700:
            target = choose_randomly(
                720,
                980, 1020
            )
        elif target == 720:
            if s != v:
                if wArray[r][s + 1] != 0:
                    target = 980
                else:
                    target = 760
            else:
                if z == 1:
                    target = 980
                else:
                    q = 1
                    target = 760
        elif target == 760:
            target = choose_randomly(
                980,
                980, 1090
            )
        elif target == 790:
            if r == h:
                target = 880
            else:
                if wArray[r + 1][s] != 0:
                    target = 880
                else:
                    if s != v:
                        if wArray[r][s + 1] != 0:
                            target = 1020
                        else:
                            target = choose_randomly(
                                1020,
                                1020, 1090
                            )
                    else:
                        if z == 1:
                            target = 1020
                        else:
                            q = 1
                            c = c + 1
                            target = 1000
        elif target == 880:
            if s != v:
                if wArray[r][s + 1] != 0:
                    target = 210
                else:
                    target = 1090
            else:
                if z == 1:
                    target = 210
                else:
                    q = 1
                    target = 1090
        elif target == 940:
            wArray[r - 1][s] = c
            c = c + 1
            vArray[r - 1][s] = 2
            r = r - 1
            if c == h * v + 1:
                target = end
            else:
                q = 0
                target = start
        elif target == 980:
            wArray[r][s - 1] = c
            c = c + 1
            target = 1000
        elif target == 1000:
            vArray[r][s - 1] = 1
            s = s - 1
            if c == h * v + 1:
                target = end
            else:
                q = 0
                target = start
        elif target == 1020:
            wArray[r + 1][s] = c
            c = c + 1
            if vArray[r][s] == 0:
                vArray[r][s] = 2
                r = r + 1
                target = 1070
            else:
                vArray[r][s] = 3
                r = r + 1
                target = 1070
        elif target == 1070:
            if c == h * v + 1:
                target = end
            else:
                target = 600
        elif target == 1090:
            if q == 1:
                z = 1
                if vArray[r][s] == 0:
                    vArray[r][s] = 1
                    q = 0
                    r = 1
                    s = 1
                    target = 260
                else:
                    vArray[r][s] = 3
                    q = 0
                    target = 210
            else:
                wArray[r][s + 1] = c
                c = c + 1
                if vArray[r][s] == 0:
                    vArray[r][s] = 1
                else:
                    vArray[r][s] = 3

                s = s + 1
                if c == v * h + 1:
                    target = end
                else:
                    target = start

    for rowIndex in range(1, v + 1):
        result = concat(result, '|')
        for i in range(1, h + 1):
            if vArray[i][rowIndex] >= 2:
                result = concat(result, '   ')
            else:
                result = concat(result, '  |')
        result = concat(result, ' ')
        result = concat(result, '\n')
        for i in range(1, h + 1):
            if vArray[i][rowIndex] == 0:
                result = concat(result, '+--')
            elif vArray[i][rowIndex] == 2:
                result = concat(result, '+--')
            else:
                result = concat(result, '+  ')
        result = concat(result, '+')
        result = concat(result, '\n')
    return result


if __name__ == '__main__':
    print doit(int(os.getenv('cols', 10)), int(os.getenv('rows', 10)))
