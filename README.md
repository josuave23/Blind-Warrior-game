# Blind-Warrior-game
(WIP) Game inspired by MagictheNoah's game on youtube. Players cannot see the board, with the goal being to either get to certain place, or to be the last player standing. Program designed with the idea of assisting the "Game Master" in keeping track of the board and enemies, but a mode for players may also be implemented.


Overall Notes
	- Want to use Adjacency Matrix to show the squares and where you can move
	- Multiple players should be allowed
	- One person designated as Game Master/ God
	- Maybe Create a player version
	

Features
	- Number of Players
	- Command List
	- Creating a Matrix
	- Assisted or Creationist Mode
		○ Will help God with prompts for Events & Enemies
	- Enemy Database & Random choice
	- Event Database & Random Choice
	- Item Starter List (Customizable)
	- Player Tokens to move
	- Player Inventory and Health
	- Player Tracker for Events and Enemies
	- (God) Shop Tracker
	- If health == 0, say player is dead
	- Random Board Generator
	

Implementation
	- At Startup, will generate a blank game board with numbered squares
		○ Asks for Assisted or Creationist
		○ Asks for number of players
		○ Asks to create adjacency list for each square (check to make sure they are adjacent) 
			§ If command generateBoard, then create a random board
		○ Ask for locations of enemies, events, shops, and portal
	- Classes
		○ Item
			§ Has Cost, Damage, and Uses
		○ Event
			§ Disappears when all players have landed on it
			§ Generates event if on Assisted mode
		○ Enemy
			§ Disappears when all players have landed on it
			§ Generates a random enemy with stats
		○ Shop
	- Commands for functions
		○ addItem : Add an Item to the list
		○ changePlayerItem : allows changes to the stats of a player's Item
		○ changeListItem : allows changes to the states of a listed item
		○ health : Prompts god to choose a player or enemy, then asks for the change in health as " +4  / -2 "
		○ gold : changes a player's gold amount (same as health)
		○ inventory : Change a players inventory, prompts for player, inventory type, and spot to change
		○ Trade : swaps items between 2 players
		○ addEnemy :adds an enemy spot on the map
		○ addEvent : adds an event spot on the map
		○ addShop : adds a shop spot on the map
		○ winner : Tells the computer that a winner has been declared, and asks for player number
		○ kill : ask for player number and reduce player to 0 hitpoints
		○ Revive : ask god how many hitpoints to revive player to
		
		
