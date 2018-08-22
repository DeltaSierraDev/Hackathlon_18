import re
N = int(input())
key_list = []
pwd_list = []
new_pwd = []
b = "backspace"
c = "caps"
new_caps = []

i = 0
while i < N:
    key_list.append(input())
    if key_list[i].isalpha() and key_list[i].islower():
        if key_list[i] != c and key_list[i] != b:
            pwd_list.append(key_list[i][0])
        else:
            pwd_list.append(key_list[i])
    i += 1
print(pwd_list)

i = 0
while i < N:
    if pwd_list[i] != b and pwd_list[i] != c:
        new_pwd.append(pwd_list[i])
    if pwd_list[i] == b:
        new_pwd.pop()
    if pwd_list[i] == c:
        new_pwd.replace()
    i += 1
print(new_pwd)


#pwd=''.join(pwd_list)
#print(pwd)
