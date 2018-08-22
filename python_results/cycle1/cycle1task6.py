import random
def random_three ():
    result =[]
    one = random.randint(0,100)
    two = random.randint(0,100)
    three = random.randint(0,100)
    result.append(one)
    result.append(two)
    result.append(three)
    return result
array = []
while True:
    array = random_three()
    if array[0]+array[1]+array[2] == 194 and array[0]*array[1]*array[2] == 229824:
        array.sort()
        break
print(array)
