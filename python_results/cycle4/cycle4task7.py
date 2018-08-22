first = input()
second = input()
first_list = []
second_list = []
new_first = []
new_second = []
for char in first:
    first_list += char
for char in second:
    second_list += char

for word in first_list:
    if word in first_list and word not in second_list:
        new_first.append(word)
    else:
        new_first.append("!")

for word in second_list:
    if word in second_list and word not in first_list:
        new_second.append(word)
    else:
        new_second.append("!")

one=''.join(new_first)
print(one)
two=''.join(new_second)
print(two)
