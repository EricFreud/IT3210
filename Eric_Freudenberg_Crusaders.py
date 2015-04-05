class Room(object):												# This is my base class for my rooms 

	def enter(self):
		pass

class Engine(object):											# This is my game engine. 

    def __init__(self, room_map):								# here I am defining the room_map	
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.starting_room()			#This is the play function, which allows the game to go from room to room. 
        last_room = self.room_map.next_room('The_End')

	while current_room != last_room:							#here is my while loop which allows the player to keep travelling through the rooms unless they die or finish. 
		next_room_name = current_room.enter()
		current_room = self.room_map.next_room(next_room_name)
		
	current_room.enter()										

class Death(Room):												# This is my death room, and is called every time the player dies. 

	def enter(self): 
		print "This will be the end of your journey."
		print "Hopefully your death will not have been in vain"
		exit(1)
		
class Introduction(Room):										#This is the first room and introduces the player to the game scenario 

	def enter(self): 
		print "You wake up in a fright to the sound of screaming and the smell of burning wood from outside of your cabin."
		print "You look outside your window and realize your entire village has been overrun by a legion of Dark Riders."
		print "One bursts into your house and points a sword at your throat."
		print "What is your name, peasant?" 
		global player_name										#This name will stick with you throughout the game
		player_name = raw_input('> ')
		print "Well %r, you have two choices. We have burned your village to the ground and there is nothing left for you here" % player_name 
		print "Our glorious victories against the Rebellion has not come without cost, and the Dark armies need recruits."
		print "If you join is, I will let you live, and you will spend the rest of your life in service to the Night Emperor."
		print "If not, I will kill you where you stand and end your pathetic life."
		print "So what will it be %r, live or die?" % player_name
		choice = raw_input('> ')								# here is the first choice the player encounters
		if choice == 'live':
			print "You take the Black Oath and swear Allegiance to the unholy Night Emperor."
			print "The next day, your camp gets ambushed by a band of Rebel Crusaders"
			print "As you try to flee, an arrow pierces you right through the chest."
			return 'Death'
		elif choice == 'die': 
			print "'I'd rather die on my feet then live on my knees!'"
			print "Kill me if you must but you will never defeat the Revolution."
			print "as the Dark Rider swings to chop off your head, you remember the dagger your father gave you before he left is strapped to your leg."
			print "You quickly grab it and lunge it into his neck." 
			print "With a look of horror and utter disbelief, he drops his sword and falls to the ground. "
			print "Now that the intruder is dead, you step out of your cabin to survey the ruins of your village."
			return 'Hometown'
		else : 
			print "invalid choice"								# This is a catch-all for any wrong input
			return 'Introduction'								# the return operator is calling a room from the room map 
		
class Hometown(Room):											#This is my Hometown room. 

	def enter(self):
		print "As you sift though the burnt rubble that once was your village, you come across a dyeing old man."
		print "Bonabus, is that you?"
		print "yes it is me, %r." % player_name 
		print "Bonabus you look terrible. Have you seen my family?"
		print "Unfortunately, your mother is no longer with us. I saw a Dark Rider dispose of her as she spat in his face."
		print "As for your sister Elysia, I saw them tie her up and drag her south towards the prison camp."
		print "And my father?"
		print "%r, They've been looking for your father Azrael since the beginning of the Revolution." % player_name
		print "Once they found him in his bunker, They were merciless." 
		print "They beat him and dragged him North towards the Dark castle to be tried as a traitor and leader of the Crusaders."
		print "You fall back as your grief overwhelms you."
		print "So what do I do Bonabus, do I head south to save my sister from the prison camp, or do I head north to save my father from execution?"  
		print "I can not make that choice for you %r. All I know is that you can not save both." % player_name
		print "Head North or South?"
		direction = raw_input('> ')								#Here is where I allowed the player to split off into two different story lines. 
		if direction == 'North': 
			return 'Troll_Bridge'
		elif direction == 'South': 
			return 'Gravewood_Pass'
		else: 
			print "invalid choice"
			return 'Hometown'
    
class GravewoodPass(Room):

	def enter(self):
		print "You decide to head South through Gravewood Pass to save your sister."
		print "As you enter the eerie wooded passageway, you get a strong feeling that you are being watched." 
		print "All of the sudden, Three Wood Sprites jump out at you from behind the trees."
		print "These are our woods intruder, and you will go no further unless you want to perish."
		print "You have 3 choices, Fight, Flee, or Persuade?"
		choice = raw_input ('> ')								#Here is the first battle choice. I have several of these in the game. 
		if choice == 'Fight': 
			print "You remember that Woodsprites are susceptible to fire."
			print "you take the lamp off the post on the side of the road and throw it at the Woodsprites."
			print "Unfortunately, you miss, and the Woodsprites ensnare you with tree limbs that squeeze the life out of you."
			return 'Death'
		elif choice == 'Flee': 
			print "You run into the woods to escape. When you stop to get your bearings, you realize you are completely lost."
			print "All of the sudden, you hear howling that could only come from one evil, disgusting looking beast."
			print "As you run in fear, a pack of Werewolves descends upon you and devourers you for lunch."
			print "Apparently, you make a very tasty Werewolf snack!"
			return 'Death' 
		elif choice == 'Persuade': 
			print "Sprites, Do you like the Night Emperor?"
			print "You mean do we like our woods being burnt down and our clans enslaved and treated as common beasts?..."
			print "No, we are not fond of the cursed Emperor and his army of thugs." 
			print "Well then join the Rebellion. My father is the leader of the Crusaders."
			print "With the help of the Woodsprites of Gravewood, you can help my father and I take down the Monster in the Castle and free us all from his tyranny!"
			print "Wait, you are %r, offspring of Azrael?" % player_name
			print "We apologize for threatening you. We have been wanting to join the Revolution for some time, but had no way to contact your father." 
			print "Well Now is your time. I speak for my father, and you are welcome to join the Crusaders. Gather your armies and head to The Dark Castle."
			print "As the Woodsprites leave, you head toward the end of the road, gaining a new ally for the Rebellion."
			return 'Prison_Camp'
		else: 
			print "invalid choice"
			return 'Gravewood_pass'
	
class PrisonCamp(Room):											#Here is my Prison Camp room 

	def enter(self):
		print "You exit out of Gravewood Pass and are now in front of the Prison camp."
		print "There are two guards standing in front of the gate." 
		print "You have two choices, Sneak-In or Fight"
		choice = raw_input('> ')								#another battle choice 
		if choice == 'Fight': 
			print "You still have your dad's trusty dagger strapped to your leg."
			print "As you approach the guards, you stop and ask them for directions."
			print "Go away you filthy peasant, we don't have time for your games."
			print "Well I have a map but I can't read it. Here let me show you."
			print "You quickly reach for your dagger and stab the first guard with the left hand, while grabbing his sword with your right hand."
			print "As the second guard raises his sword, you knock it out of his hand with the sword you took from the other guard and stab him in the chest."
			print "Now with both guards incapacitated, you walk inside the camp to find your sister."
		elif choice == 'Sneak-In':
			print "You hide behind a tree and throw a rock at the guards."
			print "As one of the guards walks over to investigate, you pick up a large tree branch and whack him in the head."
			print "As he is knocked out, you steal his uniform and put it on."
			print "As you walk past the other guard, he asks 'So what was the noise?'"
			print "I don't know, a squirl probably. I'm going to take a piss though, I'll be back"
		else:
			print "invalid choice"
			return 'Prison_Camp'
		print "Finally, you find your sister's quarters."
		print "Elysia, it's me %r! Are you ok?" % player_name
		print "Yes I'm fine, just get me out of this dreadful place"
		print "There's a lock on the door, do you know the combination?"
		print "No, you're going to have to guess."
		combination = '654'
		combo = raw_input('> ')									#here I introduce a combination lock that the player has to unlock. They get 10 tries before they are killed. 
		combos = 0 
		while combo != combination and combos < 10:				#this is the while loop that allows the player to try 10 times 
			print "try again" 
			combos += 1
			combo = raw_input('> ')
		if combo == combination: 
			print "The door unlocks, and you embrace your sister, assuring her that everything is going to be ok."
			print "After you escape from the camp, you run into a familiar face"
			print "Father!"
			print "It is me %r. While you were saving your sister, An army of Woodsprites invaded the Dark Castle and freed me from the dungeon." % player_name
			print "Together, we stormed up the tower and into the throne room, where I slew the Night Emperor as He cowered in his robes."
			print "I can't believe this. So it's all over?"
			print "No not yet. The Dark Riders still have a strong presence in the area and it will take time to eradicate them all"
			print "But if it wasn't for you %r, I would not be free and The Night Emperor would still be alive." % player_name
			print "This victory goes to you, and I am forever in your debt."
			return "The_End"
		else:
			print "After many failed attempts, you scream 'I give up!'. A guard hears you, and rushes to your position."
			print "You go to grab your sword, but you are not quick enough and the guard chops off your head."
			return 'Death' 
		
class TrollBridge(Room):										#here is my Troll Bridge Room and my second story line 

    def enter(self):
		print "As you head north, you come upon a bridge that is guarded by a large ugly troll"
		print "'Excuse me troll, but I need to pass, its a matter of life or death'"
		print "No one passes the Troll Bridge unless you answer me these riddles three." 
		print "Ok go on..."
		print "First Riddle. I am weightless but you can see me. Put me in a bucket, and I'll make it lighter. What am I?"
		choice = raw_input('> ')								#here I introduce a fun set of riddles for the player to solve 
		if choice == "a hole" or "hole":
			print "good job!"
		else: 
			print "You are thrown over the side and fall to your death."
			return 'Death'
		print "Second riddle. I have a tail and I have a head, but I have no body. What am I?"
		choice = raw_input('> ')
		if choice == "a coin" or "coin": 
			print "Excellent!"
		else:
			print "You are thrown over the side and fall to your death."
			return 'Death'
		print "Third riddle. What can run but never walks, has a mouth but never talks, has a head but never weeps, and has a bed but never sleeps?"
		choice = raw_input('> ')
		if choice == "a river" or "river": 
			print "Congratulations! You have correctly answered all three riddles. you may pass."
			return 'Dark_Castle'
		else:
			print "You are thrown over the side and fall to your death."
			return 'Death'
			
class DarkCastle(Room):										#This is my Dark Castle room 

	def enter(self):
		print "You have made it to the Dark Castle. Its massive shadow looms over all the realm. Breaking into it will not be an easy task."
		print "You only see one way in, and that's through the front door."
		print "This is do or die, If you don't get in that castle, then all will be lost."
		print "You decide to walk up to the front gate and ring the bell"
		print "The giant gate opens, and three mounted guards come out."
		print "What are you doing here?"
		print "choice 1: 'I am just wondering if I could use the bathroom'"
		print "choice 2: 'I am the offspring of Azrael, leader of the Crusaders. Prepare to die!'"
		print "choice 3: 'Aaaaaaaaggh, Zgloooorp Zig, Faaaalconima Gildash Blurgin!'"
		choice = raw_input('> ')								#here are some more choices for the player to shoose from 
		if choice == "1": 
			print "Oh you have to go to the bathroom? well there's a river flowing just below this castle, why don't you go piss in there."
			print "The guards throw you into the river, and you drown to death"
			return 'Death'
		elif choice == "2": 
			print "The guards start laughing uncontrollably."
			print "Oh you don't believe me?"
			print "As you draw your dagger from its sheath, One of the guards impales you with his spear."
			return 'Death'
		elif choice == "3": 
			print "Oh he must be that one villager the Shadow Sorcerer was experimenting on who got away."
			print "What was the Sorcerer doing to these people anyway?"
			print "I don't know, but obviously its making them completely bonkers. We better return him though, the Sorcerer was looking for him."
		else: 
			print "invalid choice"
			return 'Dark_Castle'
		print "The guards bring you to the Sorcerer's chambers and leave."
		print "As you look around, you see a shelf with three potions, one blue, one green, and one red."
		print "These potions might come in handy. Which one do I take?"
		potion = raw_input('> ')									#this is kind of a weapon choice 
		if potion == "blue": 
			print "As you take the blue potion, The Sorcerer walks into the room."
			print "What are you doing here? You are not my test subject! Guards!"
			print "You throw the blue potion in his face, and he immediately freezes in place."
			print "Now that the sorcerer is incapacitated, you take his staff, which could be used as a powerful weapon, and head for the dungeon."
			return 'Dungeon'
		if potion == "green":
			print "As you take the green potion, The Sorcerer walks into the room."
			print "What are you doing here? You are not my test subject! Guards!"
			print "You throw the green potion in his face, and he screams in agony as green vines start encapsulating him."
			print "Now that the sorcerer is incapacitated, you take his staff, which could be used as a powerful weapon, and head for the dungeon."
			return 'Dungeon'
		if potion == "red": 
			print "As you take the red potion, The Sorcerer walks into the room."
			print "What are you doing here? You are not my test subject! Guards!"
			print "You throw the red potion in his face, and he immediately bursts into flames."
			print "Now that the sorcerer is incapacitated, you take his staff, which could be used as a powerful weapon, and head for the dungeon."
			return 'Dungeon'
		else: 
			print "invalid choice"
			return "Dark_Castle"
		
	
class Dungeon(Room):											#This is my Dungeon room  

	def enter(self): 
		print "You find your way to the dungeon, and Finally set eyes on your father." 
		print "My God %r, how did you find me here?" % player_name
		print "It wasn't easy, Dad. The important question now is how do I get you out." 
		print "Well That's going to be difficult, I don't even know who has the key."
		print "Wait, I have the Shadow Staff! Dad, go to the back of your cell and cover your face."
		print "You point the Sorcerer's staff at the cell door and blast a whole in it."
		print "Well that's one way to open a door. Common dad let's get out of here."
		print "As you and your father attempt to leave, a cold, dark and ominous feeling falls over you."
		print "Suddenly, you see the Night Emperor walk down the stairs."
		print "What the hell is going on down here?" 
		print "As he sees you and your father, he becomes furious."
		print "How did you get out of your cell Azrael? and who let this little insect in to release him?"
		print "Guess your slaves aren't as competent as you thought they were, your Highness!" 
		print "Well I guess I need to take care of you two once and for all!"
		print "As the Emperor raises his Sword of Nightmares to strike, you contemplate your battle plan."
		print "Choice 1: Use the Shadow staff"
		print "Choice 2: Use your trusty dagger"
		print "Choice 3: Beg for mercy"
		choice = raw_input('> ')							#This is my last battle choice 
		if choice == "1":
			print "You point the shadow staff at the Night Emperor but it has no effect."
			print "You really think that was going to work on me? I gave that staff to the Sorcerer, I would never give one my officers a weapon they could use against me."
			print "You stupid fool! The Night Emperor swings his Sword of Nightmares and kills you and your father in one blow."
			return 'Death'
		elif choice == "2":
			print "You quickly throw your little dagger at the Emperor and it hits him square in the eye."
			print "Disoriented, he screams in agony, and drops his sword."
			print "Taking advantage of the situation, Azrael picks up the Sword of Nightmares and thrusts it though the Emperors chest."
			print "Suddenly, an ear-splitting whaling sound comes from the emperor."
			print "How could this happen? I am invincible!"
			print "As The emperor takes his last dyeing breath, Azrael looks him in the face, and says:" 
			print "'Even Tyrants, in the end, must succumb to the will of the people. As your bones are broken, so too are our chains. We are slaves to the night no longer'"
			print "As you and Azrael begin to head home, a messenger runs up to you in a hurry."
			print "Are you Azreal and %r?" % player_name 
			print "Yes, we are. What news do you bring us?"
			print "Its from Elysia, she wants you to know she escaped from the prison camp and is waiting for you in your village."
			print "You and your father begin to weep with joy."
			print "Common son, lets go home."
			return 'The_End'
		elif choice == "3": 
			print "Do you really expect me to grant you mercy? Do you two know how much trouble you have caused me? I will exterminate you right here like the vermin you are."
			print "The Night Emperor swings his Sword of Nightmares and kills you and your father in one blow."
		else: 
			return 'Death'
		
class TheEnd(Room):											#This is the last room you reach that finishes the game. 

    def enter(self):
		print "You have defeated the Night Emperor and saved the realm from eternal darkness"
		return 'The_End'
	   
class Map(object):											#This is my dictionary which holds the keywords and the rooms that are called inside the game. 

    rooms = {
		'Introduction': Introduction(),
		'Hometown' : Hometown(),
        'Gravewood_Pass': GravewoodPass(),
		'Prison_Camp' : PrisonCamp(),
        'Troll_Bridge': TrollBridge(),
        'Dark_Castle' : DarkCastle(),
        'Death': Death(),
        'The_End': TheEnd(),
		'Dungeon' : Dungeon() }

    def __init__(self, start_room):							# this defines the start_room 
        self.start_room = start_room

    def next_room(self, room_name):							#this defines how to get the rooms from the map 
        x = Map.rooms.get(room_name)
        return x

    def starting_room(self):
        return self.next_room(self.start_room)				#This defines the starting_room 

map = Map('Introduction')									#Here is where I instantiate the Map class and start it at the first room.  
game = Engine(map)											#here is where I  instantiate the Engine class with the map parameter. 
game.play()													# This is where I start the engine and the game begins 
