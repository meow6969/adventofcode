data = open("input.txt").read().split("\n")

switch = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

priorities = {}

for sack in data:
    # print(len(sack))
    # print(sack)
    sack1 = sack[:int(len(sack) / 2)]
    sack2 = sack[int(len(sack) / 2):]
    # print(sack1)
    # print(sack2)
    counted = []
    for item in sack1:
        if item in sack2 and item not in counted:
            # print(item)
            priority = 0
            priority += switch[item.lower()]
            if item.isupper():
                priority += 26
            try:
                priorities[item] += priority
            except KeyError:
                priorities[item] = priority
            counted.append(item)

# print(priorities)
score = 0
for i in priorities:
    score += priorities[i]
print(score)