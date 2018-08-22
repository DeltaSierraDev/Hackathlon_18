mystring = input()
mylist = list(mystring.lower())
newlist = list()
i=0
while i < len(mylist):
	if mylist[i].isalpha():
		newlist.append(mylist[i])
	i+=1
def count_dict(mystring):
    d = {}
    for w in mystring: 
        d[w] = mystring.count(w)
    for k in sorted(d):
        print (k + ':' + str(d[k]))
count_dict(newlist)