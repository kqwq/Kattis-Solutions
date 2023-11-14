s = input()
if ":)" in s:
    if ":(" in s:
        print("double agent")
    else:
        print("alive")
elif ":(" in s:
    print("undead")
else:
    print('machine')