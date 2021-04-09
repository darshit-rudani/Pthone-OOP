class Base(object):
	def showname(self):
		print("darshit")
	def showage(self):
		print("20")

class Chield(Base):
	def showage(self):
		print("21")

class Grandchield(Base):
	def showage(self):
		print("22")

obj1 = Base()
obj2 = Chield()
obj3 = Grandchield()

for obj4 in(obj1,obj2,obj3):
	obj4.showname()
	obj4.showage()