class Base( object ):
	def __init__(self,name):
		self.name = name

	def getname(self):
		return self.name

class Chield(Base):
	def __init__(self,name,age):
		self.age = age
		Base.__init__(self,name)

	def getage(self):
		return self.age

class Grandchield(Chield):
	def __init__(self,name,age,standred):
		self.standred = standred
		Chield.__init__(self,name,age)

	def getstandred(self):
		return self.standred

a = Grandchield("Darshit",20,"Sem 6")
print(a.getname(), a.getage(), a.getstandred())
print(a.name)
print(a.age)
print(a.standred)


