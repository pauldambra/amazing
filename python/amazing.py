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

    path_something = [[0 for _ in range(max_height + 1)] for _ in range(max_width + 1)]
    cell_exits = [[0 for _ in range(max_height + 1)] for _ in range(max_width + 1)]

    q = 0
    z = 0
    random_column = rnd(max_width)

    result = make_entry_line(max_width, random_column, result)
    result = concat(result, '\n')

    # 190
    path_something[random_column][1] = 1
    c = 2

    # 200
    x = random_column
    y = 1

    end = -1
    start = 270
    add_second_cell_exit = 940
    add_first_cell_exit = 980
    add_second_or_third_cell_exit = 1020
    check_if_can_finish = 1070

    target = start

    while target != -1:

        if target == start:
            cannot_go_left = x == 1 or path_something[x - 1][y] != 0
            cannot_go_up = y == 1 or path_something[x][y - 1] != 0
            cannot_go_right = x == max_width or path_something[x + 1][y] != 0

            if cannot_go_left:
                target = 600
            elif cannot_go_up:
                target = 430
            elif cannot_go_right:
                target = 350
            else:
                target = choose_randomly(
                    350,
                    add_second_cell_exit, add_first_cell_exit, add_second_or_third_cell_exit)
        elif target == 210:
            if x != max_width:
                x = x + 1
                target = 260
            else:
                if y != max_height:
                    x = 1
                    y = y + 1
                    target = 260
                else:
                    x = 1
                    y = 1
                    target = 260
        elif target == 260:
            if path_something[x][y] == 0:
                target = 210
            else:
                target = start
        elif target == 350:
            if y != max_height:
                if path_something[x][y + 1] != 0:
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
            if x == max_width:
                target = 530
            else:
                if path_something[x + 1][y] != 0:
                    target = 530
                else:
                    if y != max_height:
                        if path_something[x][y + 1] != 0:
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
            if y != max_height:
                if path_something[x][y + 1] != 0:
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
            cannot_go_up = y == 1 or path_something[x][y - 1] != 0
            cannot_go_right = x == max_width or path_something[x + 1][y] != 0

            if cannot_go_up:
                target = 790
            elif cannot_go_right:
                target = 720
            else:
                if y != max_height:
                    if path_something[x][y + 1] != 0:
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
            if y != max_height:
                if path_something[x][y + 1] != 0:
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
            cannot_go_right = x == max_width or path_something[x + 1][y] != 0
            if cannot_go_right:
                target = 880
            else:
                if y != max_height:
                    if path_something[x][y + 1] != 0:
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
            if y != max_height:
                if path_something[x][y + 1] != 0:
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
            path_something[x - 1][y] = c
            c = c + 1
            cell_exits[x - 1][y] = 2
            x = x - 1
            if c == max_width * max_height + 1:
                target = end
            else:
                q = 0
                target = start
        elif target == add_first_cell_exit:
            path_something[x][y - 1] = c
            c = c + 1
            cell_exits[x][y - 1] = 1
            y = y - 1
            if c == max_width * max_height + 1:
                target = end
            else:
                q = 0
                target = start
        elif target == add_second_or_third_cell_exit:
            path_something[x + 1][y] = c
            c = c + 1
            if cell_exits[x][y] == 0:
                cell_exits[x][y] = 2
                x = x + 1
                target = check_if_can_finish
            else:
                cell_exits[x][y] = 3
                x = x + 1
                target = check_if_can_finish
        elif target == check_if_can_finish:
            if c == max_width * max_height + 1:
                target = end
            else:
                target = 600
        elif target == 1090:
            '''
                so we frequently have the opportunity to jump here randomly. 
                if q is 1 we set z to 1 and reset q
                if there aren't already exits we add 1 and reset x and s. 
                otherwise there are three exits
            '''
            if q == 1:
                z = 1
                if cell_exits[x][y] == 0:
                    cell_exits[x][y] = 1
                    q = 0
                    x = 1
                    y = 1
                    target = 260
                else:
                    cell_exits[x][y] = 3
                    q = 0
                    target = 210
            else:
                path_something[x][y + 1] = c
                c = c + 1
                if cell_exits[x][y] == 0:
                    cell_exits[x][y] = 1
                else:
                    cell_exits[x][y] = 3

                y = y + 1
                if c == max_height * max_width + 1:
                    target = end
                else:
                    target = start

    print('*******')
    for thing in path_something:
        print thing

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
