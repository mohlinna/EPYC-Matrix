from sets import Set

def epyc_matrix(n):
	matrix = [[0]]
	for i in range(n-1):
		matrix.append([i+1])
		matrix[0].append(i+1)
		
	followers = []
	leftInColumns = []
	leftInRows = []
	for i in range(n):
		followers.append(Set())
		leftInColumns.append(Set())
		leftInRows.append([])
		followers[i].add(i+1)
		for j in range(n):
			if i != j:
				leftInColumns[i].add(j)
				leftInRows[i].append(j)
	find_next_element(n, matrix, followers, leftInColumns, leftInRows, 1)

def find_next_element(n, m, f, lic, lir, row):
	#print_matrix(m)
	if row == n:
		print "------------------------ Found one! --------------------"
		print_matrix(m)
	else:
		column = len(m[row])
		previous = m[row][column-1]
		lir_iterate = list(lir[row])
		row_next = row
		if column == (n-1):
			#print "Incrementing row_next"
			row_next = row + 1
		if column < row:
			value = m[column][row]
			if value in lir[row] and value in lic[column] and value not in f[previous]:
				m[row].append(value)
				lir[row].remove(value)
				lic[column].remove(value)
				f[previous].add(value)
				
				find_next_element(n, m, f, lic, lir, row_next)
				
				f[previous].remove(value)
				lic[column].add(value)
				lir[row].append(value)
				m[row].pop()
		else:
			for r in reversed(lir_iterate):
				#print "Testing %s" % numToLetter(r)
				if r in lic[column] and r not in f[previous]:
					#print "   %s works!" % numToLetter(r)
					m[row].append(r)
					lir[row].remove(r)
					lic[column].remove(r)
					f[previous].add(r)
					
					find_next_element(n, m, f, lic, lir, row_next)
					
					f[previous].remove(r)
					lic[column].add(r)
					lir[row].append(r)
					m[row].pop()
				#elif r not in lic[column]:
				#	print "   %s already used in column %d" % (numToLetter(r), column)
				#elif r in f[previous]:
				#	print "   %s has already followed %s" % (numToLetter(r), numToLetter(previous))
	
def print_matrix(m):
	print
	for row in m:
		row_string = ""
		for item in row:
			row_string += "%s "
		print row_string % tuple(map(numToLetter, row))
	print
	
def numToLetter(i):
	return str(unichr(i+97))

epyc_matrix(8)
