mystring = input()
mylist = list(mystring)
i=0
while i < len(mylist):
	if mylist[i].isalpha():
		mylist[i] = '-'
	elif mylist[i].isdigit():
		mylist[i] = '*'
	else:
		mylist[i] = '?'
	i += 1
mystring = ''.join(mylist)
print(mystring)
	