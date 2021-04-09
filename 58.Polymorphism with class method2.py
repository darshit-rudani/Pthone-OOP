class A():
	def name(self):
		print("i'm Darshit")
	def age(self):
		print("my age is 20")

class B():
	def name(self):
		print("i'm Mihir")
	def age(self):
		print("my age is 19")

obj1 = A()
obj2 = B()

for C in (obj1,obj2):
	C.name()
	C.age()