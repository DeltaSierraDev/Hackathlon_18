a = input()
a_list = a.split(" ")
o = ""
i = 0

if a_list[0] != a_list[1]:
    o = a_list[0] + ' '

while i < (len(a_list)-1):
    a_list.remove(a_list[i])
    i += 1
for char in a_list:
    o = o + char + ' '
print(o[:-1])
