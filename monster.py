import random

class Monster:
	def __init__(self, hp, strength, name):
		self.hp = hp
		self.strength = strength
		self.name = name
		
def monsterfactory_create():
	monster_names = ["Grahool", "Gruwl", "Xedgon", "Milritz", "Khaboom", "Blzorg", "Bewhat", "Gredgyll"]
	hp = random.randrange(1,10)
	strength = random.randrange(1,5)
	name = random.choice(monster_names)
	monster = Monster(hp, strength, name)
	print(f"created monster {name} [{hp},{strength}]")
	return monster
