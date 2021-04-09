class person:

	def __init__(self,name,age):
		self.n = name
		self.a = age

	def details(self):
		print(self.n, self.a)

p1 = person('darshit',20)

p1.details()
