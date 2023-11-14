import sys

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def nToWord(n, capitalize=False):
  # print(n)
  if n <= 19:
    output = ones[n]
  else:
    tensDigit = n // 10
    onesDigit = n % 10
    output = ""
    output = tens[tensDigit]
    if onesDigit > 0:
      output += "-" + ones[onesDigit]
  if capitalize:
    return output[0].upper()+output[1:]
  else:
    return output


for line in sys.stdin:
  words = line.split()
  for i, word in enumerate(words):
    if word.isnumeric() and int(word) <= 99:
      words[i] = nToWord(int(word), i == 0)
  print(" ".join(words))
