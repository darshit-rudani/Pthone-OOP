class Student( object ):

	def __init__(self , name ,age):
		self.name = name
		self.age = age
	def display(self):
		print(self.name)
		print(self.age)

class Marks(Student):
	def __init__(self,name,age,mark):
		self.mark = mark
		Student.__init__(self,name,age)

a = Marks("dd",22,100)
a.display()
print(a.mark)