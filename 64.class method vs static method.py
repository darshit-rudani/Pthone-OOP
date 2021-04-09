from datetime import date 

class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
	
	@classmethod
	def fromBirthYear(self, name, year): 
		return self(name, date.today().year - year) 
	
	@staticmethod
	def isAdult(age): 
		return age > 18

person1 = Person('Darshit', 20) 
person2 = Person.fromBirthYear('Darshit', 2001) 

print(person1.name)
print(person1.age)
print(person2.name) 
print(person2.age) 

print (Person.isAdult(20)) 
