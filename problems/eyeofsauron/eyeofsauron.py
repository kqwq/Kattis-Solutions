s = input()

if "()" in s and s.find("()") == len(s) / 2 - 1:
    print("correct")
else:
    print("fix")