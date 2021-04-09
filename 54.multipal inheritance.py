class Base(object):
	def __init__(self,name):
		self.name = name

	def display():
		print(self.name)

class Chield(object):
	def __init__(self,name,age):
		self.age = age
		Base.__init__(self,name)

class Grandchield(Base,Chield):
	def __init__(self,name,age,study):
		self.study = study
		Chield.__init__(self,name,age)

a = Grandchield("Darshit",20,"Sem 6")

print(a.name)
print(a.age)
print(a.study)