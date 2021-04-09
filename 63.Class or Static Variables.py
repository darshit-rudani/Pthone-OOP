class person:
	stream = 'cse'				 
	def __init__(self,name,roll):
		self.name = name		 
		self.roll = roll		 

a = person('Geek', 1)
b = person('Nerd', 2)

print(a.stream) 
print(b.stream) 
print(a.name) 
print(b.name) 
print(a.roll) 
print(b.roll) 

print(person.stream) 

a.stream = 'ece'
print(a.stream) 
print(b.stream) 

person.stream = 'mech'

print(a.stream) 
print(b.stream) 
