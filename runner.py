from player import Player
from monster import *
from room import *

if __name__ == "__main__":
	print("welcome to fight club")
	player = Player(10,2)
	
	rooms = [Room("You enter the first room. You can see three doors in the distance..."), Room("This is the final room. Select you faith...")]
	room_index = 0

	while room_index < len(rooms):
		current_room = rooms[room_index]
		print(current_room.description)

		selected_door = int(input("which door? (1-3)")) - 1
		if current_room.items[selected_door] == Item.MONSTER:
			monster = monsterfactory_create()
			print(f"you encounter {monster.name}")
			player.fight(monster)
		elif current_room.items[selected_door] == Item.TREASURE:
			print("you find some fancy gold!")
			pass
		elif current_room.items[selected_door] == Item.EMPTY:
			print("there's nothing behind the door. Phew!")
			pass

		room_index += 1
