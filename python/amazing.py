#! env python

import os
import random

WHEN_CANNOT_GO_RIGHT = 350
WHEN_CANNOT_GO_UP = 430
WHEN_CANNOT_GO_LEFT = 600
ADD_SECOND_CELL_EXIT = 940
ADD_FIRST_CELL_EXIT = 980
ADD_SECOND_OR_THIRD_CELL_EXIT = 1020
CHECK_IF_CAN_FINISH = 1070


def concat(r, text):
    return r + text


def rnd(count):
    return random.randint(1, count + 1)


def make_entry_line(max_width, random_gate_pos):
    entry_line = ''

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

    if max_width == 1 or max_height == 1:
        return

    path_something = [[0 for _ in range(max_height + 1)] for _ in range(max_width + 1)]
    cell_exits = [[0 for _ in range(max_height + 1)] for _ in range(max_width + 1)]

    found_exit = False  # whenever this is set to true x and y are the co-ords of the exit
    z = 0
    entry_column = rnd(max_width)

    # 190
    path_something[entry_column][1] = 1
    current_step = 2

    # 200
    x = entry_column
    y = 1

    end = -1
    start = 270

    target = start

    while target != -1:

        if target == start:
            cannot_go_left = x == 1 or path_something[x - 1][y] != 0
            cannot_go_up = y == 1 or path_something[x][y - 1] != 0
            cannot_go_right = x == max_width or path_something[x + 1][y] != 0

            if cannot_go_left:
                target = WHEN_CANNOT_GO_LEFT
            elif cannot_go_up:
                target = WHEN_CANNOT_GO_UP
            elif cannot_go_right:
                target = WHEN_CANNOT_GO_RIGHT
            else:
                target = choose_randomly(
                    WHEN_CANNOT_GO_RIGHT,
                    ADD_SECOND_CELL_EXIT, ADD_FIRST_CELL_EXIT, ADD_SECOND_OR_THIRD_CELL_EXIT)
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
        elif target == WHEN_CANNOT_GO_RIGHT:
            if y != max_height:
                if path_something[x][y + 1] != 0:
                    target = 410
                else:
                    target = 390
            else:
                if z == 1:
                    target = 410
                else:
                    found_exit = True
                    print('set q... x:' + str(x) + ' y:' + str(y))
                    target = 390
        elif target == 390:
            target = choose_randomly(
                410,
                ADD_SECOND_CELL_EXIT, ADD_FIRST_CELL_EXIT, 1090
            )
        elif target == 410:
            target = choose_randomly(
                WHEN_CANNOT_GO_UP,
                ADD_SECOND_CELL_EXIT, ADD_FIRST_CELL_EXIT
            )
        elif target == WHEN_CANNOT_GO_UP:
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
                            found_exit = True
                            print('set q... x:' + str(x) + ' y:' + str(y))
                            target = 500
        elif target == 500:
            target = choose_randomly(
                510,
                ADD_SECOND_CELL_EXIT, ADD_SECOND_OR_THIRD_CELL_EXIT, 1090
            )
        elif target == 510:
            target = choose_randomly(
                530,
                ADD_SECOND_CELL_EXIT, ADD_SECOND_OR_THIRD_CELL_EXIT
            )
        elif target == 530:
            if y != max_height:
                if path_something[x][y + 1] != 0:
                    target = ADD_SECOND_CELL_EXIT
                else:
                    target = 570
            else:
                if z == 1:
                    target = ADD_SECOND_CELL_EXIT
                else:
                    found_exit = True
                    print('set q... x:' + str(x) + ' y:' + str(y))
                    target = 570
        elif target == 570:
            target = choose_randomly(
                ADD_SECOND_CELL_EXIT,
                ADD_SECOND_CELL_EXIT, 1090
            )
        elif target == WHEN_CANNOT_GO_LEFT:
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
                        found_exit = True
                        print('set q... x:' + str(x) + ' y:' + str(y))
                        target = 680
        elif target == 680:
            target = choose_randomly(
                700,
                ADD_FIRST_CELL_EXIT, ADD_SECOND_OR_THIRD_CELL_EXIT, 1090
            )
        elif target == 700:
            target = choose_randomly(
                720,
                ADD_FIRST_CELL_EXIT, ADD_SECOND_OR_THIRD_CELL_EXIT
            )
        elif target == 720:
            if y != max_height:
                if path_something[x][y + 1] != 0:
                    target = ADD_FIRST_CELL_EXIT
                else:
                    target = 760
            else:
                if z == 1:
                    target = ADD_FIRST_CELL_EXIT
                else:
                    found_exit = True
                    print('set q... x:' + str(x) + ' y:' + str(y))
                    target = 760
        elif target == 760:
            target = choose_randomly(
                ADD_FIRST_CELL_EXIT,
                ADD_FIRST_CELL_EXIT, 1090
            )
        elif target == 790:
            cannot_go_right = x == max_width or path_something[x + 1][y] != 0
            if cannot_go_right:
                target = 880
            else:
                if y != max_height:
                    if path_something[x][y + 1] != 0:
                        target = ADD_SECOND_OR_THIRD_CELL_EXIT
                    else:
                        target = choose_randomly(
                            ADD_SECOND_OR_THIRD_CELL_EXIT,
                            ADD_SECOND_OR_THIRD_CELL_EXIT, 1090
                        )
                else:
                    if z == 1:
                        target = ADD_SECOND_OR_THIRD_CELL_EXIT
                    else:
                        found_exit = True
                        print('set q... x:' + str(x) + ' y:' + str(y))
                        current_step = current_step + 1
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
                    found_exit = True
                    print('set q... x:' + str(x) + ' y:' + str(y))
                    target = 1090
        elif target == ADD_SECOND_CELL_EXIT:
            path_something[x - 1][y] = current_step
            current_step = current_step + 1
            cell_exits[x - 1][y] = 2
            x = x - 1
            if current_step == max_width * max_height + 1:
                target = end
            else:
                found_exit = False
                target = start
        elif target == ADD_FIRST_CELL_EXIT:
            path_something[x][y - 1] = current_step
            current_step = current_step + 1
            cell_exits[x][y - 1] = 1
            y = y - 1
            if current_step == max_width * max_height + 1:
                target = end
            else:
                found_exit = False
                target = start
        elif target == ADD_SECOND_OR_THIRD_CELL_EXIT:
            path_something[x + 1][y] = current_step
            current_step = current_step + 1
            if cell_exits[x][y] == 0:
                cell_exits[x][y] = 2
                x = x + 1
                target = CHECK_IF_CAN_FINISH
            else:
                cell_exits[x][y] = 3
                x = x + 1
                target = CHECK_IF_CAN_FINISH
        elif target == CHECK_IF_CAN_FINISH:
            if current_step == max_width * max_height + 1:
                target = end
            else:
                target = WHEN_CANNOT_GO_LEFT
        elif target == 1090:
            '''
                so we frequently have the opportunity to jump here randomly. 
                if q is 1 we set z to 1 and reset q
                if there aren't already exits we add 1 and reset x and s. 
                otherwise there are three exits
            '''
            if found_exit:
                z = 1
                if cell_exits[x][y] == 0:
                    cell_exits[x][y] = 1
                    found_exit = False
                    x = 1
                    y = 1
                    target = 260
                else:
                    cell_exits[x][y] = 3
                    found_exit = False
                    target = 210
            else:
                path_something[x][y + 1] = current_step
                current_step = current_step + 1
                if cell_exits[x][y] == 0:
                    cell_exits[x][y] = 1
                else:
                    cell_exits[x][y] = 3

                y = y + 1
                if current_step == max_height * max_width + 1:
                    target = end
                else:
                    target = start

    print('*******')
    for thing in path_something:
        print thing

    return draw_maze(cell_exits, entry_column, max_height, max_width)


def draw_maze(cell_exits, entry_column, max_height, max_width):
    header = 'Amazing - Copyright by Creative Computing, Morristown, NJ\n'
    result = concat(header, make_entry_line(max_width, entry_column))
    result = concat(result, '\n')
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
