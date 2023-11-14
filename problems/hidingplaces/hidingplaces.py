n = int(input())


def setBoard(board, i, j, ifIsSetTo, setTo):
    if i < 0 or i >= 8 or j < 0 or j >= 8:
        return
    if board[i][j] == ifIsSetTo:
        board[i][j] = setTo


for i in range(n):
    line = input()
    x = ord(line[0])-97
    y = int(line[1])-1
    # print('x', x, y)

    board = [[0] * 8 for _ in range(8)]
    board[y][x] = 1

    for look in range(1, 10):
        for i in range(8):
            for j in range(8):
                if board[i][j] == look:
                    setBoard(board, i+1, j+2, 0, look+1)
                    setBoard(board, i+2, j+1, 0, look+1)
                    setBoard(board, i-1, j-2, 0, look+1)
                    setBoard(board, i-2, j-1, 0, look+1)
                    setBoard(board, i+1, j-2, 0, look+1)
                    setBoard(board, i+2, j-1, 0, look+1)
                    setBoard(board, i-1, j+2, 0, look+1)
                    setBoard(board, i-2, j+1, 0, look+1)

    # ok we're done, let's find the locations of the max value
    # find max value
    maxVal = 0
    for i in range(8):
        for j in range(8):
            maxVal = max(maxVal, board[i][j])

    # find poses
    pos = []

    for i in range(7,-1,-1):
        for j in range(8):
            if board[i][j] == maxVal:
                pos.append(chr(97+j)+str(i+1))

    print(maxVal-1, *pos)
