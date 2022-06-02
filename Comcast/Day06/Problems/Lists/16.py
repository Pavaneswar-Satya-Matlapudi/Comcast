l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
output = []

def removeNestings(l):
	for i in l:
		if type(i) == list:
			removeNestings(i)
		else:
			output.append(i)
removeNestings(l)
print ('The list after removing nesting: ', output)
