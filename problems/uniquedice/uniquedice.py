def getDiceId(die: list):
    # Rotate die to numbers are as close to 6 5 4 3 2 1 as possible
    # Prioritize big numbers near the beginning

    # If they are all the same
    if die.count(die[0]) == 6:
        return str(die[0])*6

    # Score the 3 face pairs and determine if we need to rotate clockwise or anti-clockwise
    pair1 = die[0:2]
    pair2 = die[2:4]
    pair3 = die[4:6]
    score1 = max(pair1) * 6 + min(pair1)
    score2 = max(pair2) * 6 + min(pair2)
    score3 = max(pair3) * 6 + min(pair3) 

    # If 2 sides are dominant, make them cancel out
    if score1 == score2:
        score1 = 0
        score2 = 0
    elif score1 == score3:
        score1 = 0
        score3 = 0
    elif score2 == score3:
        score2 = 0
        score3 = 0

    if score2 > score1 and score2 > score3:
        # Rotate clockwise (shift down 2)
        die = die[2:6] + [ die[0], die[1]]
    elif score3 > score1 and score3 > score2:
        # Rotate anti-clockwise (shift up 2)
        die = [die[4], die[5]] + die[0:4]

   # Now that the dominate side is in the first 2 indexes, make higher side on top
    if die[0] < die[1]:
        die = [die[1], die[0],  die[5], die[4], die[3], die[2]]

    # Now that the dominate side is at the top, rotate until we get the "best" orientation
    bestScore = -1
    bestLast4 = None
    last4 = die[2:6]
    for i in range(0, 4):
        last4 = [last4[3], last4[2], last4[0], last4[1]]
        score = last4[0] * 6**3 +\
            last4[1] * 6**2 +\
            last4[2] * 6**1 +\
            last4[3] * 6**0
        if score > bestScore:
            bestLast4 = last4
            bestScore = score

    # If the top and bottom sides are the same, flip it for good measure
    if die[0] == die[1]:
        die = [die[1], die[0],  die[5], die[4], die[3], die[2]]  
    last4 = die[2:6]
    for i2 in range(0, 4):
        last4 = [last4[3], last4[2], last4[0], last4[1]]
        score = last4[0] * 6**3 +\
            last4[1] * 6**2 +\
            last4[2] * 6**1 +\
            last4[3] * 6**0
        if score > bestScore:
            bestLast4 = last4
            bestScore = score  
        
    die = die[0:2] + bestLast4

    return "".join(map(str, die))

n = int(input())
hash = {}
for i in range(n):
    die = list(map(int, input().split()))
    did = getDiceId(die) # Turn distict dice into unique IDs
    if did in hash:
        hash[did] += 1
    else:
        hash[did] = 1

print(max(hash.values()))
