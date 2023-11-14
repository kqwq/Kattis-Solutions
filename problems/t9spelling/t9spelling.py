
n = int(input())
keypad = {
  "a": 2,
  "b": 22,
  "c": 222,
  "d": 3,
  "e": 33,
  "f": 333,
  "g": 4,
  "h": 44,
  "i": 444,
  "j": 5,
  "k": 55,
  "l": 555,
  "m": 6,
  "n": 66,
  "o": 666,
  "p": 7,
  "q": 77,
  "r": 777,
  "s": 7777,
  "t": 8,
  "u": 88,
  "v": 888,
  "w": 9,
  "x": 99,
  "y": 999,
  "z": 9999,
  " ": 0,
}

for i in range(n):
  s = input()
  out = ""
  lastValFirst = "~"
  for c in s:
    val = str(keypad[c])
    if val[0] == lastValFirst:
      out += " "
    out += str(keypad[c])
    lastValFirst = val[0]


  print("Case #" + str(i+1) + ":", out)