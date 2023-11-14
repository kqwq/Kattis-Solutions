
n = int(input())
for i in range(n):
  message = input()
  messageLen = len(message)
  messageRows = int(messageLen ** 0.5)
  decoded = ""
  for y in range(messageRows):
    for x in range(messageRows):
      xRot =  messageRows - y - 1
      yRot = x

      index = yRot * messageRows + xRot
      decoded += message[index]
  print(decoded)
