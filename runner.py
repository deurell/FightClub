from player import Player
from monster import *

if __name__ == "__main__":
	print("welcome to fight club")
	player = Player(10,2)
	
	while player.hp > 0:		
		#create monster with a factory method
		monster = monsterfactory_create()
		# player, fight the monster!
		player.fight(monster)

