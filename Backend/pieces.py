class Pawn:
	def canAccessPosition(self, joueur, x, y, newX, newY):
		if 1 <= x <= 8 and 1 <= y <= 8 and 1 <= newX <= 8 and 1 <= newY <= 8:
			if [newX, newY] in self.getAvailablePositions(x, y):
				return True
			else:
				return False
		else:
			return False
			
	def getAvailablePositions(self, joueur, x, y):
		arr = []
		if joueur == 0:
			if y == 2:
				arr.append([x, y + 2])
				arr.append([x, y + 1])
				arr.append([x - 1, y + 1])
				arr.append([x + 1, y + 1])
			else:
				arr.append([x, y + 1])
				arr.append([x + 1, y + 1])
				arr.append([x - 1, y + 1])
		else:
			if y == 7:
				arr.append([x, y - 2])
				arr.append([x, y - 1])
				arr.append([x - 1, y - 1])
				arr.append([x + 1, y - 1])
			else:				
				arr.append([x, y - 1])
				arr.append([x + 1, y - 1])
				arr.append([x - 1, y - 1])
		return arr
		
class King:
	def canAccessPosition(self, joueur, x, y, newX, newY):
		if 1 <= x <= 8 and 1 <= y <= 8 and 1 <= newX <= 8 and 1 <= newY <= 8:
			if [newX, newY] in self.getAvailablePositions(x, y):
				return True
			else:
				return False
		else:
			return False
			
	def getAvailablePositions(self, x, y):
		arr = []
		arr.append([x, y - 1])
		arr.append([x + 1, y - 1])
		arr.append([x + 1, y])
		arr.append([x + 1, y + 1])
		arr.append([x, y + 1])
		arr.append([x - 1, y + 1])
		arr.append([x - 1, y])
		arr.append([x - 1, y - 1])
		return arr

class Knight:
	def canAccessPosition(self, joueur, x, y, newX, newY):
		if 1 <= x <= 8 and 1 <= y <= 8 and 1 <= newX <= 8 and 1 <= newY <= 8:
			if [newX, newY] in self.getAvailablePositions(x, y):
				return True
			else:
				return False
		else:
			return False
		
	def getAvailablePositions(self, x, y):
		arr = []
		arr.append([y + 2, x + 1])
		arr.append([y + 2, x - 1])
		arr.append([y + 1, x + 2])
		arr.append([y - 1, x + 2])
		arr.append([y - 2, x + 1])
		arr.append([y - 2, x - 1])
		arr.append([y + 1, x - 2])
		arr.append([y - 1, x - 2])
	
		for i in range(0, len(arr)): #[y, x] parceque je suis un noob. Reverse pour avoir [x, y] parceque la flemme de changer l'ordre
			arr[i].reverse()
	
		return arr
		

class Rook:
	def canAccessPosition(self, joueur, x, y, newX, newY):
		if 1 <= x <= 8 and 1 <= y <= 8 and 1 <= newX <= 8 and 1 <= newY <= 8:
			if [newX, newY] in self.getAvailablePositions(x, y):
				return True
			else:
				return False
		else:
			return False
	
	def getAvailablePositions(self, x, y):
		arr = []
		for i in range(-8, 8):
			if 1 <= (x + i) <= 8 and 1 <= (y + i) <= 8 and i != 0: #Diag de haut gauche a bas droit
				#print('X : ' + str(x + i) + ' Y : ' + str(y + i)) 
				arr.append([x + i, y + i])
			if 1 <= (x - i) <= 8 and 1 <= (y + i) <= 8 and i != 0: #Diag haut droit bas gauche
				#print('2 : X : ' + str(x - i) + ' Y : ' + str(y + i))
				arr.append([x - i, y + i])
		return arr
r = Rook()
print(r.canAccessPosition(1, 4, 5, 1, 2))
			
			
			
			
			
			
			
			
		
		