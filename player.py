from monster import Monster
import random

class Player():
	
	def __init__(self, hp, strength):
		self.hp = hp
		self.strength = strength
		
	def attack(self, monster):
		# 50% chance to win
		win = True
		if random.random() > 0.5:
			self.hp = self.hp - monster.strength
			print(f"{monster.name} wins attack. Player hp {self.hp}")
		else:
			monster.hp = monster.hp - self.strength
			print(f"player wins attack. Monster hp {monster.hp}")
				
	def fight(self, monster):
		print("fighting monster")
		fighting = True
		while fighting:
			self.attack(monster)
			if self.hp <= 0:
				print("player dead, game over")
				fighting = False
			elif monster.hp <= 0:
				print(f"{monster.name} is dead, congrats!")
				fighting = False
			
