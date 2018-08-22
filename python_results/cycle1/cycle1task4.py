s = input()

def not_bad(s):
	notV = s.find('not') 
	badV = s.find('bad') 
	if (badV > notV): 
		return s[:notV] + 'good' + s[(badV+3):]
	return s
		
print(not_bad(s))