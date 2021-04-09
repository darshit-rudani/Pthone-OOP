class Person( object ):
	def __init__(self , name):
		self.name = name
	def display(self):
		print(self.name)

class Address(Person):
	def __init__(self,name,address):
		self.address = address
		Person.__init__(self,name)

class Age(Address):
	def __init__(self,name,address,age):
		self.age = age
		Address.__init__(self,name,address)

a = Age("Darshit","Surat",20)

a.display()
print(a.address)
print(a.age)