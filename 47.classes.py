class MyClass:
  x = 5

print(MyClass)


p1 = MyClass()

print(p1.x)

class Person:
  def __init__(self,name, age):
    self.n = name
    self.a = age

p1 = Person("John", 36)

print(p1.n)
print(p1.a)

class droke:
	def __init__(my,name,age):
		my.n = name
		my.a = age

p2 = droke("darshit" , 20)

p2.a = 21

print(p2.a)