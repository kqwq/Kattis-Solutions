s = input().split(" ")
words = set()
for w in s:
    if w in words:
        print("no")
        quit()
    words.add(w)
print("yes")
