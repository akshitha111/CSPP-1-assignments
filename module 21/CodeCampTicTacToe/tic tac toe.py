def checkInput(matrix):
	for i in matrix:
		for j in i:
			if j not in "o x .":
				return False
	return True
def CheckGame(matrix):
	count_o = 0
	count_x = 0
	for row in matrix:
		for i in row:
			if i == 'o':
				count_o += 1
			elif i == 'x':
				count_x += 1
	if abs(count_o-count_x == 1) or abs(count_0-count_x == 0):
		return True
	return False

def rows(matrix):
	winner_x = False
	winner_o = False
	if row.count("x") == 3:
		winner_x = True
	if row.count("o") == 3:
		winner_o = True
	if winner_o and winner_x:
		print("invalid game")
		exit()
	if winner_x:
		return (True,"x")
	if winner_o:
		return (True,"o")
def column(matrix):
	transpose = []
	for i in range(len(matrix)):
		row = []
		for j in range(len(matrix[0])):
			row.append(matrix[j][i])
		transpose.append(row)
	return rows(transpose)
def diagonal(matrix):
	d1 = []
	for i in range(len(matrix)):
		d1.append[matrix[i][i]]
	if d1.count("o") == 3:
		return (True,"o")
	if d1.count("x") == 3:
		return (True,"x")
	d2 = []
	j = len(matrix[0])-1
	for i in range(len(matrix)):
		d2.append(matrix[i][j])
		j = j-1
	if d2.count("o") == 3:
		return
	if d2.count("x") == 3:
		return
	return (False,0)





def main():
	matrix = []
	i = 0
	while i < 3:
		lst = input().split(" ")
		matrix.append(lst)
		i = i + 1
		print(matrix)
		if checkGame(matrix):
			checkWinner
		else:
			print("Invalid game")
	if checkInput(matrix):
		main()