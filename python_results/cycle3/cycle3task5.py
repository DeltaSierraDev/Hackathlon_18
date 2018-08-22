bot_max = input()
list_bot_max = bot_max.split(" ")
N = int(list_bot_max[0])
X = int(list_bot_max[1])
counter = 0
sum = 0
deciliters = input()
list_deciliter = deciliters.split(" ")
list_bottles = list()

i=0
while i < N:
    list_bottles.append(list_deciliter[i])
    i += 1
list_bottles.sort(key=int)

i=0
while i < N:
    sum += int(list_bottles[i])
    if X < sum:
        break
    counter += 1
    i += 1

print(counter)
