alphabet = input()
code = input()
out = ""
for i in range(0, len(code), 3):
    key = int(code[i:i+3])-1
    out += alphabet[key]
print(out)