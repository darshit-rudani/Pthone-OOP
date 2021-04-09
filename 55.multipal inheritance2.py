class Base( object ):
	def __init__(self):
		self.name = "Darshit"
		print("hii")

class Chield:
	def __init__(self):
		self.name2 = "Uv"
		print("hiii")

class Grandchield(Base,Chield):
	def __init__(self):
		print("Derive")
		Base.__init__(self)
		Chield.__init__(self)

	def printstr(self):
		print(self.name,self.name2)

a = Grandchield()
a.printstr()