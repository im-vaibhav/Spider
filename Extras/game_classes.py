"""
Basic game format.
Making enemy class 
OOP in python
"""

class Enemy:
	life = 3

	def attack(self):
		print("ouch!")
		self.life -= 1
	
	def checkLife(self):
		if self.life <= 0
			print('I\'m Dead')
		else:
			print(str(self.life) + "life left")

enemy1 = Enemy()

enemy1.attack()
enemy1.checkLife()