import time
import os as o

o.system('cls')
move = "0"
def clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6):
    o.system('cls')
    print("                                 _      __")
    print("                                | |    / _|")
    print("   __ ___  _ __  _ __   ___  ___| |_  | |_ ___  _   _ _ __")
    print(" / __/ _ \| '_ \| '_ \ / _ \/ __| __| |  _/ _ \| | | | '__|")
    print(" |(_| (_) | | | | | | |  __/ (__| |_  | || (_) | |_| | |")
    print(" \___\___/|_| |_|_| |_|\___|\___|\__| |_| \___/ \__,_|_|")

    print("")
    print("")
    print("")
    print("._________________________________.")
    print(tStr1)
    print(tStr2)
    print(tStr3)
    print(tStr4)
    print(tStr5)
    print(tStr6)
    print(" ‾|‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|‾|‾")
    print("  ‾‾‾                         ‾‾‾")

tStr1 = ["_", "_", "_", "_", "_", "_", "_"]
tStr2 = ["_", "_", "_", "_", "_", "_", "_"]
tStr3 = ["_", "_", "_", "_", "_", "_", "_"]
tStr4 = ["_", "_", "_", "_", "_", "_", "_"]
tStr5 = ["_", "_", "_", "_", "_", "_", "_"]
tStr6 = ["_", "_", "_", "_", "_", "_", "_"]

def checkMoveP1(move):
    if tStr6[int(move) - 1] == "_":
        tStr6[int(move) - 1]  = "X"
    elif tStr5[int(move) - 1] == "_":
        tStr5[int(move) - 1] = "X"
    elif tStr4[int(move) - 1] == "_":
        tStr4[int(move) - 1] = "X"
    elif tStr3[int(move) - 1] == "_":
        tStr3[int(move) - 1] = "X"
    elif tStr2[int(move) - 1] == "_":
        tStr2[int(move) - 1] = "X"
    elif tStr1[int(move) - 1] == "_":
        tStr1[int(move) - 1] = "X"

def checkMoveP2(move2):
    if tStr6[int(move2) - 1] == "_":
        tStr6[int(move2) - 1] = "O"
    elif tStr5[int(move2) - 1] == "_":
        tStr5[int(move2) - 1] = "O"
    elif tStr4[int(move2) - 1] == "_":
        tStr4[int(move2) - 1] = "O"
    elif tStr3[int(move2) - 1] == "_":
        tStr3[int(move2) - 1] = "O"
    elif tStr2[int(move2) - 1] == "_":
        tStr2[int(move2) - 1] = "O"
    elif tStr1[int(move2) - 1] == "_":
        tStr1[int(move2) - 1] = "O"

def p1move():
    move = input("Player 1: ")

    if move == "1":
        checkMoveP1(int(move))
    elif move == "2":
        checkMoveP1(int(move))
    elif move == "3":
        checkMoveP1(int(move))
    elif move == "4":
        checkMoveP1(int(move))
    elif move == "5":
        checkMoveP1(int(move))
    elif move == "6":
        checkMoveP1(int(move))
    elif move == "7":
        checkMoveP1(int(move))
    else:
        print("Only type numbers 1-7. Please refresh to restart.")
        breakpoint

def p2move():
    move2 = input("Player 2: ")

    if move2 == "1":
        checkMoveP2(int(move2))
    elif move2 == "2":
        checkMoveP2(int(move2))
    elif move2 == "3":
        checkMoveP2(int(move2))
    elif move2 == "4":
        checkMoveP2(int(move2))
    elif move2 == "5":
        checkMoveP2(int(move2))
    elif move2 == "6":
        checkMoveP2(int(move2))
    elif move2 == "7":
        checkMoveP2(int(move2))
    else:
        print("Only type numbers 1-7. Please refresh to restart.")

win = False
stop = False

def checkWinHorisontalX6(win):
    numX = 0
    repeat = True
    for i in tStr6:
        if i == "X":
            repeat = True
            numX += 1
            if numX == 4:
                win = True
                repeat = False
                break
        elif i == "O" or i == "_":
            numX = 0

    return win

def checkWinHorisontalX5(win):
    numX = 0
    repeat = True
    for i in tStr5:
        if i == "X":
            repeat = True
            numX += 1
            if numX == 4:
                win = True
                repeat = False
                break
        elif i == "O" or i == "_":
            numX = 0

    return win

def checkWinHorisontalX4(win):
    numX = 0
    repeat = True
    for i in tStr4:
        if i == "X":
            repeat = True
            numX += 1
            if numX == 4:
                win = True
                repeat = False
                break
        elif i == "O" or i == "_":
            numX = 0

    return win

def checkWinHorisontalX3(win):
    numX = 0
    repeat = True
    for i in tStr3:
        if i == "X":
            repeat = True
            numX += 1
            if numX == 4:
                win = True
                repeat = False
                break
        elif i == "O" or i == "_":
            numX = 0

    return win

def checkWinHorisontalX2(win):
    numX = 0
    repeat = True
    for i in tStr2:
        if i == "X":
            repeat = True
            numX += 1
            if numX == 4:
                win = True
                repeat = False
                break
        elif i == "O" or i == "_":
            numX = 0

    return win

def checkWinHorisontalX1(win):
    numX = 0
    repeat = True
    for i in tStr1:
        if i == "X":
            repeat = True
            numX += 1
            if numX == 4:
                win = True
                repeat = False
                break
        elif i == "O" or i == "_":
            numX = 0

    return win


def checkWinHorisontalO6(win):
    numO = 0
    repeat = True
    for i in tStr6:
        if i == "O":
            repeat = True
            numO += 1
            if numO == 4:
                win = True
                repeat = False
                break
        elif i == "X" or i == "_":
            numO = 0

    return win

def checkWinHorisontalO5(win):
    numO = 0
    repeat = True
    for i in tStr5:
        if i == "O":
            repeat = True
            numO += 1
            if numO == 4:
                win = True
                repeat = False
                break
        elif i == "X" or i == "_":
            numO = 0

    return win

def checkWinHorisontalO4(win):
    numO = 0
    repeat = True
    for i in tStr4:
        if i == "O":
            repeat = True
            numO += 1
            if numO == 4:
                win = True
                repeat = False
                break
        elif i == "X" or i == "_":
            numO = 0

    return win

def checkWinHorisontalO3(win):
    numO = 0
    repeat = True
    for i in tStr3:
        if i == "O":
            repeat = True
            numO += 1
            if numO == 4:
                win = True
                repeat = False
                break
        elif i == "X" or i == "_":
            numO = 0

    return win

def checkWinHorisontalO2(win):
    numO = 0
    repeat = True
    for i in tStr2:
        if i == "O":
            repeat = True
            numO += 1
            if numO == 4:
                win = True
                repeat = False
                break
        elif i == "X" or i == "_":
            numO = 0

    return win

def checkWinHorisontalO1(win):
    numO = 0
    repeat = True
    for i in tStr1:
        if i == "O":
            repeat = True
            numO += 1
            if numO == 4:
                win = True
                repeat = False
                break
        elif i == "X" or i == "_":
            numO = 0

    return win


def checkWinVerticalX1(win):
    vumX = 0
    for i in tStr6:
        vumX += 1
        if i == "X":
            if tStr5[vumX - 1] == "X":
                if tStr4[vumX - 1] == "X":
                    if tStr3[vumX - 1] == "X":
                        win = True
                        break
    return win

def checkWinVerticalX2(win):
    vumX = 0
    for i in tStr5:
        vumX += 1
        if i == "X":
            if tStr4[vumX - 1] == "X":
                if tStr3[vumX - 1] == "X":
                    if tStr2[vumX - 1] == "X":
                        win = True
                        break
    return win

def checkWinVerticalX3(win):
    vumX = 0
    for i in tStr4:
        vumX += 1
        if i == "X":
            if tStr3[vumX - 1] == "X":
                if tStr2[vumX - 1] == "X":
                    if tStr1[vumX - 1] == "X":
                        win = True
                        break
    return win


def checkWinVerticalO1(win):
    vumO = 0
    for i in tStr6:
        vumO += 1
        if i == "O":
            if tStr5[vumO - 1] == "O":
                if tStr4[vumO - 1] == "O":
                    if tStr3[vumO - 1] == "O":
                        win = True
                        break
    return win

def checkWinVerticalO2(win):
    vumO = 0
    for i in tStr5:
        vumO += 1
        if i == "O":
            if tStr4[vumO - 1] == "O":
                if tStr3[vumO - 1] == "O":
                    if tStr2[vumO - 1] == "O":
                        win = True
                        break
    return win

def checkWinVerticalO3(win):
    vumO = 0
    for i in tStr4:
        vumO += 1
        if i == "X":
            if tStr3[vumO - 1] == "O":
                if tStr2[vumO - 1] == "O":
                    if tStr1[vumO - 1] == "O":
                        win = True
                        break
    return win

while win == False and stop == False:
    clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
    p1move()
    if checkWinHorisontalX6(win) == True or checkWinHorisontalX5(win) == True or checkWinHorisontalX4(win) == True or checkWinHorisontalX3(win) == True or checkWinHorisontalX2(win) == True or checkWinHorisontalX1(win) == True:
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 1 wins!")
        break
    if checkWinVerticalX1(win) == True: #  <--- Problem
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 1 Wins!")
        break
    if checkWinVerticalX2(win) == True:
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 1 Wins!")
        break
    if checkWinVerticalX3(win) == True:
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 1 Wins!")
        break
    clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
    p2move()
    if checkWinHorisontalO6(win) == True or checkWinHorisontalO5(win) == True or checkWinHorisontalO4(win) == True or checkWinHorisontalO3(win) == True or checkWinHorisontalO2(win) == True or checkWinHorisontalO1(win) == True:
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 2 Wins!")
        break
    if checkWinVerticalO1(win) == True:
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 2 Wins!")
        break
    if checkWinVerticalO2(win) == True:
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 2 Wins!")
        break
    if checkWinVerticalO3(win) == True:
        clear(tStr1, tStr2, tStr3, tStr4, tStr5, tStr6)
        print("Player 2 Wins!")
        break