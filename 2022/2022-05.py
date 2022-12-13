data = open("input.txt").read().split("\n")



for i, line in enumerate(data):
    if line[1].isdigit():
        counting_y = i
        break

# print(counting_y)

# for i in range(counting_y + 2):
#     print(i)

mult = 4
pointer = 1
counting_x = 0
meowing = True
while meowing:
    # print(data[counting_y][pointer])
    try:
        if data[counting_y][pointer].isdigit():
            counting_x += 1 
        else:
            meowing = False
    except IndexError:
        meowing = False
    pointer += mult
# print(counting_x)

# for y in range(counting_y, -1, -1):
#     line = data[y]
#     for x in range(counting_x):

crates = []

print(data)

for x in range(counting_x):
    stack = []
    for y in range(counting_y, -1, -1):
        
        print(y)
       
        if x == 0:
            val = 1 
        else:
            val = x * mult
        print(x * mult)
        if data[y][val].isdigit():
            stack.append(data[y][x * mult])
    crates.append(stack)
print(crates)
    
    
