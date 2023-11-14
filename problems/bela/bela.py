


scores = {
    "A": [11,11],
    "K": [4,4],
    "Q": [3,3],
    "J": [20,2],
    "T": [10,10],
    "9": [14,0],
    "8": [0,0],
    "7": [0,0]
}

n_, suit = input().split()
n=int(n_)
total = 0
for i in range(n * 4):
    hand = input()
    isDom = hand[1] == suit
    if isDom:
        total += scores[hand[0]][0]
    else:
        total += scores[hand[0]][1]
print(total)