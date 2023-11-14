"""
Algorithm 

Iterate every cell

- Update goesDown until there are no more updates
- Answer is (# of cells - goesDown)

"""


x, y = map(int, input().split())

goesDown = []
garden = []
for i in range(y):
    garden.append(list(map(int, input().split())))
    goesDown.append([False] * x)


change = True
while change:
    change = False
    for j in range(y):
        for i in range(x):
            if not goesDown[j][i]:
                # Curr level
                curr = garden[j][i]
                walls = [
                    {"condition": j > 0, "x": i, "y": j - 1},
                    {"condition": j < y-1, "x": i, "y": j + 1},
                    {"condition": i > 0, "x": i-1, "y": j },
                    {"condition": i < x-1, "x": i+1, "y": j },
                ]

                for wall in walls:
                  # Check upper
                  if not wall['condition']:
                      continue
                  higherThanSur = curr - garden[wall["y"]][wall["x"]]
                  if  (higherThanSur == 0 and goesDown[wall["y"]][wall["x"]]) or higherThanSur > 0:
                      goesDown[j][i] = True
                      change = True

    for j in range(y-1, -1, -1):
        for i in range(x-1, -1, -1):
            if not goesDown[j][i]:
                # Curr level
                curr = garden[j][i]
                walls = [
                    {"condition": j > 0, "x": i, "y": j - 1},
                    {"condition": j < y-1, "x": i, "y": j + 1},
                    {"condition": i > 0, "x": i-1, "y": j },
                    {"condition": i < x-1, "x": i+1, "y": j },
                ]

                for wall in walls:
                  # Check upper
                  if not wall['condition']:
                      continue
                  higherThanSur = curr - garden[wall["y"]][wall["x"]]
                  if  (higherThanSur == 0 and goesDown[wall["y"]][wall["x"]]) or higherThanSur > 0:
                      goesDown[j][i] = True
                      change = True


      

# Count goesDown
goesDownCount = 0
for row in goesDown:
    for cell in row:
        goesDownCount += cell

print(x * y - goesDownCount)
