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


def choose_randomly(default, *targets):
    x = rnd(len(targets))
    if x > len(targets):
        return default
    return targets[x - 1]


def doit(max_width, max_height):

    result = 'Amazing - Copyright by Creative Computing, Morristown, NJ\n'

    if max_width == 1 or max_height == 1:
        return

    w_array = [[0 for _ in range(max_height + 1)] for _ in range(max_width + 1)]
    cell_exits = [[0 for _ in range(max_height + 1)] for _ in range(max_width + 1)]

    q = 0
    z = 0
    random_column = rnd(max_width)

    result = make_entry_line(max_width, random_column, result)
    result = concat(result, '\n')

    # 190
    w_array[random_column][1] = 1
    c = 2

    # 200
    r = random_column
    s = 1

    start = 270
    end = -1
    add_second_cell_exit = 940
    add_first_cell_exit = 980
    add_second_or_third_cell_exit = 1020
    check_if_can_finish = 1070

    target = start

    while target != -1:
        if target == start:
            if r - 1 == 0:
                target = 600
            else:
                if w_array[r - 1][s] != 0:
                    target = 600
                else:
                    if s - 1 == 0:
                        target = 430
                    else:
                        if w_array[r][s - 1] != 0:
                            target = 430
                        else:
                            if r == max_width:
                                target = 350
                            else:
                                if w_array[r + 1][s] != 0:
                                    target = 350
                                else:
                                    target = choose_randomly(
                                        350,
                                        add_second_cell_exit, add_first_cell_exit, add_second_or_third_cell_exit)
        elif target == 210:
            if r != max_width:
                r = r + 1
                target = 260
            else:
                if s != max_height:
                    r = 1
                    s = s + 1
                    target = 260
                else:
                    r = 1
                    s = 1
                    target = 260
        elif target == 260:
            if w_array[r][s] == 0:
                target = 210
            else:
                target = start
        elif target == 350:
            if s != max_height:
                if w_array[r][s + 1] != 0:
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
                add_second_cell_exit, add_first_cell_exit, 1090
            )
        elif target == 410:
            target = choose_randomly(
                430,
                add_second_cell_exit, add_first_cell_exit
            )
        elif target == 430:
            if r == max_width:
                target = 530
            else:
                if w_array[r + 1][s] != 0:
                    target = 530
                else:
                    if s != max_height:
                        if w_array[r][s + 1] != 0:
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
                add_second_cell_exit, add_second_or_third_cell_exit, 1090
            )
        elif target == 510:
            target = choose_randomly(
                530,
                add_second_cell_exit, add_second_or_third_cell_exit
            )
        elif target == 530:
            if s != max_height:
                if w_array[r][s + 1] != 0:
                    target = add_second_cell_exit
                else:
                    target = 570
            else:
                if z == 1:
                    target = add_second_cell_exit
                else:
                    q = 1
                    target = 570
        elif target == 570:
            target = choose_randomly(
                add_second_cell_exit,
                add_second_cell_exit, 1090
            )
        elif target == 600:
            if s - 1 == 0:
                target = 790
            else:
                if w_array[r][s - 1] != 0:
                    target = 790
                else:
                    if r == max_width:
                        target = 720
                    else:
                        if w_array[r + 1][s] != 0:
                            target = 720
                        else:
                            if s != max_height:
                                if w_array[r][s + 1] != 0:
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
                add_first_cell_exit, add_second_or_third_cell_exit, 1090
            )
        elif target == 700:
            target = choose_randomly(
                720,
                add_first_cell_exit, add_second_or_third_cell_exit
            )
        elif target == 720:
            if s != max_height:
                if w_array[r][s + 1] != 0:
                    target = add_first_cell_exit
                else:
                    target = 760
            else:
                if z == 1:
                    target = add_first_cell_exit
                else:
                    q = 1
                    target = 760
        elif target == 760:
            target = choose_randomly(
                add_first_cell_exit,
                add_first_cell_exit, 1090
            )
        elif target == 790:
            if r == max_width:
                target = 880
            else:
                if w_array[r + 1][s] != 0:
                    target = 880
                else:
                    if s != max_height:
                        if w_array[r][s + 1] != 0:
                            target = add_second_or_third_cell_exit
                        else:
                            target = choose_randomly(
                                add_second_or_third_cell_exit,
                                add_second_or_third_cell_exit, 1090
                            )
                    else:
                        if z == 1:
                            target = add_second_or_third_cell_exit
                        else:
                            q = 1
                            c = c + 1
                            target = 1000
        elif target == 880:
            if s != max_height:
                if w_array[r][s + 1] != 0:
                    target = 210
                else:
                    target = 1090
            else:
                if z == 1:
                    target = 210
                else:
                    q = 1
                    target = 1090
        elif target == add_second_cell_exit:
            w_array[r - 1][s] = c
            c = c + 1
            cell_exits[r - 1][s] = 2
            r = r - 1
            if c == max_width * max_height + 1:
                target = end
            else:
                q = 0
                target = start
        elif target == add_first_cell_exit:
            w_array[r][s - 1] = c
            c = c + 1
            cell_exits[r][s - 1] = 1
            s = s - 1
            if c == max_width * max_height + 1:
                target = end
            else:
                q = 0
                target = start
        elif target == add_second_or_third_cell_exit:
            w_array[r + 1][s] = c
            c = c + 1
            if cell_exits[r][s] == 0:
                cell_exits[r][s] = 2
                r = r + 1
                target = check_if_can_finish
            else:
                cell_exits[r][s] = 3
                r = r + 1
                target = check_if_can_finish
        elif target == check_if_can_finish:
            if c == max_width * max_height + 1:
                target = end
            else:
                target = 600
        elif target == 1090:
            if q == 1:
                z = 1
                if cell_exits[r][s] == 0:
                    cell_exits[r][s] = 1
                    q = 0
                    r = 1
                    s = 1
                    target = 260
                else:
                    cell_exits[r][s] = 3
                    q = 0
                    target = 210
            else:
                w_array[r][s + 1] = c
                c = c + 1
                if cell_exits[r][s] == 0:
                    cell_exits[r][s] = 1
                else:
                    cell_exits[r][s] = 3

                s = s + 1
                if c == max_height * max_width + 1:
                    target = end
                else:
                    target = start

    print('*******')
    print w_array

    for rowIndex in range(1, max_height + 1):
        result = concat(result, '|')
        for colIndex in range(1, max_width + 1):
            if cell_exits[colIndex][rowIndex] >= 2:
                result = concat(result, '   ')
            else:
                result = concat(result, '  |')
        result = concat(result, ' ')
        result = concat(result, '\n')
        for colIndex in range(1, max_width + 1):
            if cell_exits[colIndex][rowIndex] % 2 == 0:
                result = concat(result, '+--')
            else:
                result = concat(result, '+  ')
        result = concat(result, '+')
        result = concat(result, '\n')
    return result


if __name__ == '__main__':
    print doit(int(os.getenv('cols', 10)), int(os.getenv('rows', 10)))
