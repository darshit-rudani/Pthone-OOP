class Square: 
	def __init__(self): 
		pass

class SquarePrism(Square): 
	def __init__(self): 
		pass

class Cube(SquarePrism): 
	def __init__(self): 
		pass

square = Square() 
squareprism = SquarePrism() 
cube = Cube() 

print(isinstance(squareprism, Square)) 
print(isinstance(cube, Square)) 
