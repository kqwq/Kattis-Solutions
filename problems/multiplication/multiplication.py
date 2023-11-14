

while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        quit()

    aDigits = list(map(int, str(a)))
    bDigits = list(map(int, str(b)))

    # Define grid
    grid = []
    gridW = 2 + 2 + 1 + 4 * len(aDigits)
    gridH = 2 + 2 + 1 + 4 * len(bDigits)
    for i in range(gridH):
        grid.append([" "] * gridW)

    # Grid outer border
    # Top and bottom edges
    for edge in [0, gridH-1]:
        for i in range(gridW):
            grid[edge][i] = "-"
    # Left and right edges
    for side in [0, gridW-1]:
        for i in range(gridH):
            if i == 0 or i == gridH - 1:
                grid[i][side] = "+"
            else:
                grid[i][side] = "|"

    # Grid boxes
    for i in range(len(bDigits)):
        for j in range(len(aDigits)):
            for lesserYPos in range(0, 5):
                for lesserXPos in range(0, 5):
                    greaterYPos = 2 + i * 4
                    greaterXPos = 2 + j * 4
                    char = " "
                    if lesserXPos == 4 - lesserYPos:
                        char = "/"
                    if lesserXPos == 0 or lesserXPos == 4:
                        if lesserYPos == 0 or lesserYPos == 4:
                            char = "+"
                        else:
                            char = "|"
                    elif lesserYPos == 0 or lesserYPos == 4:
                        char = "-"
                    grid[greaterYPos+lesserYPos][greaterXPos+lesserXPos] = char

    # Top number (a)
    for i, digit in enumerate(aDigits):
        grid[1][4 + 4 * i] = str(digit)

    # Right number (a)
    for i, digit in enumerate(bDigits):
        grid[4 + 4 * i][gridW-2] = str(digit)

    # Internal boxes
    for (i, bDig) in enumerate(bDigits):
      for (j, aDig) in enumerate(aDigits):
          product = bDig * aDig
          productStr = str(product)
          first = 0
          second = 0
          if product >= 10:
              first = int(productStr[0])
              second = int(productStr[1])
          else:
              second = int(productStr)
          midPosX = 4 + 4 * j
          midPosY = 4 + 4 * i
          grid[midPosY-1][midPosX-1] = str(first)
          grid[midPosY+1][midPosX+1] = str(second)

    # Wrap-around numbers
    c = a * b
    cDigitsStr = str(c)
    div1 = cDigitsStr[len(cDigitsStr)-len(aDigits):]
    div2 = cDigitsStr[0:len(cDigitsStr)-len(aDigits)]
    ## Bottom portion
    for (i, cDig) in enumerate(div1):
      xPos = 3 + 4 * i
      yPos = gridH - 2
      grid[yPos][xPos] = cDig
      if i < len(aDigits)-1:
        grid[yPos][xPos + 2] = "/"
    ## Left portion
    for (i, cDig) in enumerate(div2[::-1]):
      xPos = 1
      yPos = gridH -4 - 4 * i
      grid[yPos][xPos] = cDig
      grid[yPos+2][xPos] = "/"        


    # Print out
    for row in grid:
        print("".join(row))
