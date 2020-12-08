gameover = False
square = 1
while gameover == False:
    roll = int(input())
    if square + roll > 100:
        square = square
    else:
        square = square + roll
    if square == 9:
        square = 34
    if square == 40:
        square =64
    if square == 67:
        square = 86
    if square == 54:
        square = 19
    if square == 90:
        square = 48
    if square == 99:
        square = 77
    if roll == 0:
        gameover = True
        print("You Quit!")
    if gameover == False:
        print("You are now on square", square)
    if square == 100:
        print("You Win!")
        gameover = True
