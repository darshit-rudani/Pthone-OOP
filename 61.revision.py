# Singal inheritance
print('Singal................................................................')
print(' ')

class base(object):
	def __init__(self,name):
		self.name = name

	def display(self):
		print(self.name)

class chield(base):
	def __init__(self,name,age):
		self.age = age

		base.__init__(self,name)

a = chield('darshit',20)
a.display()

print(" ")
print("multilevel............................................................")
print(' ')

#  multilevel inheritance

class base(object):
	def __init__(self,name):
		self.name = name

	def display(self):
		print(self.name)

class chield(base):
	def __init__(self,name,age):
		self.age = age

		base.__init__(self,name)

	def display2(self):
		print(self.age)

class grandchield(chield):
	def __init__(self,name,age,study):
		self.study = study

		chield.__init__(self,name,age)

	def display3(self):
		print(self.study)


a = grandchield('darshit',20,'6th sem')
a.display()
a.display2()
a.display3()

print(' ')
print('multipal.............................................................. ')
print(' ')

class base2(object):
	def __init__(self,name):
		self.name = name

	def display(self):
		print(self.name)

class chield2(object):
	def __init__(self,age):
		self.age = age

	def display2(self):
		print(self.age)

class grandcield2(base2,chield2):
	def __init__(self,name,age,study):
		self.study = study

		base2.__init__(self,name)
		chield2.__init__(self,age)

	def display3(self):
		print(self.study)

a = grandcield2('mihir',21,'5th sem')

a.display()
a.display2()
a.display3()


print(' ')
print('polymorphism with class mithod........................................')
print(' ')

class person(object):
	def displayname(self):
		print("Darshit")

	def displayage(self):
		print("i am 20 years old")

class person2(object):
	def displayname(self):
		print("mihir")

	def displayage(self):
		print("i am 19 years old")

a = person()
b = person2()

a.displayname()
a.displayage()
b.displayname()
b.displayage()


print(' ')
print('polymorphism with inheritance.........................................')
print(' ')

class A(object):
	def displayname(self):
		print("darshit")

	def displayage(self):
		print(20)

class B(A):
	def displayage(self):
		print(21)

class C(B):
	def displayage(self):
		print(22)

obj1 = A()
obj2 = B()
obj3 = C()

for D in(obj1,obj2,obj3):
	D.displayname()
	D.displayage()

obj1.displayname()
obj1.displayage()
obj2.displayname()
obj2.displayage()
obj3.displayname()
obj3.displayage()

print(' ')
print('polymorphism with function and object.................................')
print(' ')

class first():

	def name(self):
		print("Darshit")
	def age(self):
		print(20)

class second():
	def name(self):
		print("jenish")
	def age(self):
		print(23)

def third(obj):
	obj.name()
	obj.age()

obj_first = first()
obj_second = second()

third(obj_first)
third(obj_second)
