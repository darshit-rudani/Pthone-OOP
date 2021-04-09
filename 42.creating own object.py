class player:
	
	membership = True
	def __init__(self, name , age):
		if (self.membership):
			self.name = name
			self.age = age

	def run(self):
		print(f'my name is {self.name}')


player1 = player('darshit',18)
player2 = player('yash',17)
player2.attact = 50


print(player1.run())
print(player2.age)

