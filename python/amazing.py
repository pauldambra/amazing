#! env python

import os
import random


def println(r):
    return r + '\n'

def write(text, r):
    return r + text

def rnd(count):
    return random.randint(1, count+1)

def doit(horizontal, vertical):

    target = 0
    result = ''

    result = write('Amazing - Copyright by Creative Computing, Morristown, NJ', result)
    result = println(result)

    h = horizontal
    v = vertical
    if h == 1 or v == 1:
        return

    wArray = [[0 for x in range(v+1)] for y in range(h+1)]
    vArray = [[0 for x in range(v+1)] for y in range(h+1)]

    q = 0
    z = 0
    x = rnd(h)

    # 130:170
    for i in range(1, h+1):
        if i == x:
            result = write('+  ', result)
        else:
            result = write('+--', result)

    # 180
    result = write('+', result)
    result = println(result)

    # 190
    c = 1
    wArray[x][1] = c
    c = c+1

    # 200
    r = x
    s = 1
    target = 270

    while target != -1:
        if target == 210:
            if r != h:
                target = 250
            else:
                target = 220
        elif target == 220:
            if s != v:
                target = 240
            else:
                target = 230
        elif target == 230:
            r = 1
            s = 1
            target = 260
        elif target == 240:
            r = 1
            s = s+1
            target = 260
        elif target == 250:
            r = r+1
            target = 260
        elif target == 260:
            if wArray[r][s] == 0:
                target = 210
            else:
                target = 270
        elif target == 270:
            if r - 1 == 0:
                target = 600
            else:
                target = 280
        elif target == 280:
            if wArray[r - 1][s] != 0:
                target = 600
            else:
                target = 290
        elif target == 290:
            if s - 1 == 0:
                target = 430
            else:
                target = 300
        elif target == 300:
            if wArray[r][s - 1] != 0:
                target = 430
            else:
                target = 310
        elif target == 310:
            if r == h:
                target = 350
            else:
                target = 320
        elif target == 320:
            if wArray[r + 1][s] != 0:
                target = 350
            else:
                target = 330
        elif target == 330:
            x = rnd(3)
            target = 340
        elif target == 340:
            if x == 1:
                target = 940
            elif x == 2:
                target = 980
            elif x == 3:
                target = 1020
            else:
                target = 350
        elif target == 350:
            if s != v:
                target = 380
            else:
                target = 360
        elif target == 360:
            if z == 1:
                target = 410
            else:
                target = 370
        elif target == 370:
            q = 1
            target = 390
        elif target == 380:
            if wArray[r][s + 1] != 0:
                target = 410
            else:
                target = 390
        elif target == 390:
            x = rnd(3)
            target = 400
        elif target == 400:
            if x == 1:
                target = 940
            elif x == 2:
                target = 980
            elif x == 3:
                target = 1090
            else:
                target = 410
        elif target == 410:
            x = rnd(2)
            target = 420
        elif target == 420:
            if x == 1:
                target = 940
            elif x == 2:
                target = 980
            else:
                target = 430
        elif target == 430:
            if r == h:
                target = 530
            else:
                target = 440
        elif target == 440:
            if wArray[r + 1][s] != 0:
                target = 530
            else:
                target = 450
        elif target == 450:
            if s != v:
                target = 480
            else:
                target = 460
        elif target == 460:
            if z == 1:
                target = 510
            else:
                target = 470
        elif target == 470:
            q = 1
            target = 490
        elif target == 480:
            if wArray[r][s + 1] != 0:
                target = 510
            else:
                target = 490
        elif target == 490:
            x = rnd(3)
            target = 500
        elif target == 500:
            if x == 1:
                target = 940
            elif x == 2:
                target = 1020
            elif x == 3:
                target = 1090
            else:
                target = 510
        elif target == 510:
            x = rnd(2)
            target = 520
        elif target == 520:
            if x == 1:
                target = 940
            elif x == 2:
                target = 1020
            else:
                target = 530
        elif target == 530:
            if s != v:
                target = 560
            else:
                target = 540
        elif target == 540:
            if z == 1:
                target = 590
            else:
                target = 550
        elif target == 550:
            q = 1
            target = 570
        elif target == 560:
            if wArray[r][s + 1] != 0:
                target = 590
            else:
                target = 570
        elif target == 570:
            x = rnd(2)
            target = 580
        elif target == 580:
            if x == 1:
                target = 940
            elif x == 2:
                target = 1090
            else:
                target = 590
        elif target == 590:
            target = 940
        elif target == 600:
            if s - 1 == 0:
                target = 790
            else:
                target = 610
        elif target == 610:
            if wArray[r][s - 1] != 0:
                target = 790
            else:
                target = 620
        elif target == 620:
            if r == h:
                target = 720
            else:
                target = 630
        elif target == 630:
            if wArray[r + 1][s] != 0:
                target = 720
            else:
                target = 640
        elif target == 640:
            if s != v:
                target = 670
            else:
                target = 650
        elif target == 650:
            if z == 1:
                target = 700
            else:
                target = 660
        elif target == 660:
            q = 1
            target = 680
        elif target == 670:
            if wArray[r][s + 1] != 0:
                target = 700
            else:
                target = 680
        elif target == 680:
            x = rnd(3)
            target = 690
        elif target == 690:
            if x == 1:
                target = 980
            elif x == 2:
                target = 1020
            elif x == 3:
                target = 1090
            else:
                target = 700
        elif target == 700:
            x = rnd(2)
            target = 710
        elif target == 710:
            if x == 1:
                target = 980
            elif x == 2:
                target = 1020
            else:
                target = 720
        elif target == 720:
            if s != v:
                target = 750
            else:
                target = 730
        elif target == 730:
            if z == 1:
                target = 780
            else:
                target = 740
        elif target == 740:
            q = 1
            target = 760
        elif target == 750:
            if wArray[r][s + 1] != 0:
                target = 780
            else:
                target = 760
        elif target == 760:
            x = rnd(2)
            target = 770
        elif target == 770:
            if x == 1:
                target = 980
            elif x == 2:
                target = 1090
            else:
                target = 780
        elif target == 780:
            target = 980
        elif target == 790:
            if r == h:
                target = 880
            else:
                target = 800
        elif target == 800:
            if wArray[r + 1][s] != 0:
                target = 880
            else:
                target = 810
        elif target == 810:
            if s != v:
                target = 840
            else:
                target = 820
        elif target == 820:
            if z == 1:
                target = 870
            else:
                target = 830
        elif target == 830:
            q = 1
            target = 990
        elif target == 840:
            if wArray[r][s + 1] != 0:
                target = 870
            else:
                target = 850
        elif target == 850:
            x = rnd(2)
            target = 860
        elif target == 860:
            if x == 1:
                target = 1020
            elif x == 2:
                target = 1090
            else:
                target = 870
        elif target == 870:
            target = 1020
        elif target == 880:
            if s != v:
                target = 910
            else:
                target = 890
        elif target == 890:
            if z == 1:
                target = 930
            else:
                target = 900
        elif target == 900:
            q = 1
            target = 920
        elif target == 910:
            if wArray[r][s + 1] != 0:
                target = 930
            else:
                target = 920
        elif target == 920:
            target = 1090
        elif target == 930:
            target = 1190
        elif target == 940:
            wArray[r - 1][s] = c
            target = 950
        elif target == 950:
            c = c+1
            vArray[r - 1][s] = 2
            r = r-1
            target = 960
        elif target == 960:
            if c == h * v + 1:
                target = 1200
            else:
                target = 970
        elif target == 970:
            q = 0
            target = 270
        elif target == 980:
            wArray[r][s - 1] = c
            target = 990
        elif target == 990:
            c = c+1
            target = 1000
        elif target == 1000:
            vArray[r][s - 1] = 1
            s = s-1
            if c == h * v + 1:
                target = 1200
            else:
                target = 1010
        elif target == 1010:
            q = 0
            target = 270
        elif target == 1020:
            wArray[r + 1][s] = c
            target = 1030
        elif target == 1030:
            c = c+1
            if vArray[r][s] == 0:
                target = 1050
            else:
                target = 1040
        elif target == 1040:
            vArray[r][s] = 3
            target = 1060
        elif target == 1050:
            vArray[r][s] = 2
            target = 1060
        elif target == 1060:
            r = r+1
            target = 1070
        elif target == 1070:
            if c == h * v + 1:
                target = 1200
            else:
                target = 1080
        elif target == 1080:
            target = 600
        elif target == 1090:
            if q == 1:
                target = 1150
            else:
                target = 1100
        elif target == 1100:
            wArray[r][s + 1] = c
            c = c+1
            if vArray[r][s] == 0:
                target = 1120
            else:
                target = 1110
        elif target == 1110:
            vArray[r][s] = 3
            target = 1130
        elif target == 1120:
            vArray[r][s] = 1
            target = 1130
        elif target == 1130:
            s = s+1
            if c == v * h + 1:
                target = 1200
            else:
                target = 1140
        elif target == 1140:
            target = 270
        elif target == 1150:
            z = 1
            target = 1160
        elif target == 1160:
            if vArray[r][s] == 0:
                target = 1180
            else:
                target = 1170
        elif target == 1170:
            vArray[r][s] = 3
            q = 0
            target = 1190
        elif target == 1180:
            vArray[r][s] = 1
            q = 0
            r = 1
            s = 1
            target = 260
        elif target == 1190:
            target = 210
        elif target == 1200:
            target = -1

    for j in range(1, v+1):
        result = write('|', result)
        for i in range(1, h+1):
            if vArray[i][j] >= 2:
                result = write('   ', result)
            else:
                result = write('  |', result)
        result = write(' ', result)
        result = println(result)
        for i in range(1, h+1):
            if vArray[i][j] == 0:
                result = write('+--', result)
            elif vArray[i][j] == 2:
                result = write('+--', result)
            else:
                result = write('+  ', result)
        result = write('+', result)
        result = println(result)
    return result

if __name__ == '__main__':
    print doit(int(os.getenv('cols', 10)), int(os.getenv('rows', 10)))

