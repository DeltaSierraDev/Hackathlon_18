my_string = input()
my_list = list(my_string)
x=my_string[0]
i=0
while i<len(my_string):
	if my_list[i] == x:
		my_list[i] = '*'
	i += 1
my_list[0]=x
my_string=''.join(my_list)
print(my_string)