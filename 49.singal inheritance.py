class person:

	def __init__(self,name):
		self.name = name

	def getname(self):
		return self.name

	def employe(self):
		return False

class person2(person):

	def employe(self):
		return True

emp = person2("employe2")
print(emp.getname(),emp.employe())
