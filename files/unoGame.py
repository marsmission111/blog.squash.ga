print
print 'Welcome to uno.exe!'
print 'This program was made by Ryan Curry using Python 2.7'
print 'To find out more, read the README file'
print
print

#creates README file
READMEtext = 'This program was made by Ryan Curry using Python 2.7\nTo find an indepth discussion on the creation of this program, or the .py file, go to blog.squash.ga\n\nThank you for downloading this program, hope you enjoy :)'
README = open('README.txt', 'w+')
README.write(READMEtext)
README.close()


import random	#imports random

#Initializes deck and shuffles it
global unoDeck
global unoDiscard
uno = ['yellow_0', 'red_0', 'green_0', 'blue_0', 'yellow_1', 'red_1', 'green_1', 'blue_1', 'yellow_2', 'red_2', 'green_2', 'blue_2', 'yellow_3', 'red_3', 'green_3', 'blue_3', 'yellow_4', 'red_4', 'green_4', 'blue_4', 'yellow_5', 'red_5', 'green_5', 'blue_5', 'yellow_6', 'red_6', 'green_6', 'blue_6', 'yellow_7', 'red_7', 'green_7', 'blue_7', 'yellow_8', 'red_8', 'green_8', 'blue_8', 'yellow_9', 'red_9', 'green_9', 'blue_9', 'yellow_reverse', 'red_reverse', 'green_reverse', 'blue_reverse', 'yellow_reverse', 'red_reverse', 'green_reverse', 'blue_reverse', 'yellow_drawTwo', 'red_drawTwo', 'green_drawTwo', 'blue_drawTwo', 'yellow_drawTwo', 'red_drawTwo', 'green_drawTwo', 'blue_drawTwo', 'wild_wild', 'wild_wildDraw4', 'wild_wild', 'wild_wildDraw4', 'wild_wild', 'wild_wildDraw4', 'wild_wild', 'wild_wildDraw4', 'wild_wild', 'wild_wildDraw4']
unoDeck = []
bufferDeck = uno
unoDiscard = []
adminDeck = uno


#Variables players are computer intances and users are the people
while True:
	try:
		deckNum = int(raw_input('Enter number of UNO decks to play with: '))
		if deckNum <= 0:
			print 'ENter value greater than 0'
			continue
		if deckNum == 69: print 'Weird Flex but OK'
		for i in range(deckNum):
			for card in uno:
				unoDeck.append(card)
		random.shuffle(unoDeck)
		playerNum = int(raw_input("Enter number of computers: "))
		userNum = int(raw_input("Enter number of users: "))
		handSize = int(raw_input('Hand Size: '))
		while handSize <= 0:
			print 'Enter hand size greater than 0'
			handSize = int(raw_input('Hand Size: '))
		playerLst = []
		usrLst = []
		if (playerNum + userNum) * handSize >= (len(unoDeck)-(len(usrLst)+len(playerLst)+4)):	#the minus 4 is just a buffer so if players draw cards the chance of error is lower
			print "There are not enough cards to satisfy your lust of large games of UNO"
			continue
		if playerNum <= 4 and userNum <= 0:
			print 'There needs to be more than 4 CPU players when the computer plays itself'
			continue
		print
		break
	except:
		print 'Enter valid entries!'




#Functions for drawcard and init dealing
def addCard(player, discard):
	global unoDiscard
	global unoDeck
	while True:
		try:
			player.append(unoDeck[0])
			unoDeck.remove(unoDeck[0])
			break
		except:
			print '\r' + 'There are no more cards in the deck! Reshuffling discard.'
			if len(unoDiscard) == 0:
				outInput = raw_input('Out of cards, would you like to randomly add a card to the discard pile? [y,n]: ')
				if outInput == 'y':
					random.shuffle(bufferDeck)
					unoDiscard.append(bufferDeck[0])
				else:
					print 'Cannot draw cards, exiting game'
					exit()
			for card in unoDiscard:
				unoDeck.append(card)
			unoDiscard = []
			unoDiscard.append(unoDeck[-1])
			unoDeck.pop(-1)
			random.shuffle(unoDeck)
			break

def playCard(player, card):
	print 'Card was played: ' + str(card)
	try:
		player.remove(card)
		unoDiscard.append(card)
	except:
		checkWinner(player)

def checkWinner(player, unoDiscard):
	if len(player) == 0:
		print
		print masterLst[0] + ' won the game'
		raw_input('Press Enter to exit')
		exit()

def dealer(player, handSize):
	for i in range(handSize):
		addCard(player, unoDiscard)

def reverse(master):
	global masterLst
	masterLst = master[::-1]	#reverses players

def wild(player):
	yellowCount = 0
	blueCount = 0
	greenCount = 0
	redCount = 0

	for card in player:
		if card.split("_")[0] == "wild" and card.split("_")[1] == "wild":	
			for cards in player:	#count the color of cards in the player list
				if cards.split("_")[0] == "yellow": 
					yellowCount += 1
				if cards.split("_")[0] == "green": 
					greenCount += 1
				if cards.split("_")[0] == "red": 
					redCount += 1
				if cards.split("_")[0] == "blue": 
					blueCount += 1

			#checks max type of card
			playCard(player, card)	#plays the actual wild card
			if yellowCount >= max(greenCount, redCount, blueCount): 			
				unoDiscard.append('yellow_wildT')
				return True
			if greenCount >= max(redCount, blueCount, yellowCount): 
				unoDiscard.append('green_wildT')
				return True
			if redCount >= max(blueCount, yellowCount, greenCount): 
				unoDiscard.append('red_wildT')
				return True
			if blueCount >= max(yellowCount, greenCount, redCount): 
				unoDiscard.append('blue_wildT')
				return True

			#this line of code is IF there is a weird error while calculating max
			else: 
				unoDiscard.append("blue_wildT")
				return True


def user(user):

	for i in range(len(masterLst)):
		if len(globals()[masterLst[i]]) == 1:
			print str(masterLst[i])+ ' has one card left!!'
	#added if line because my dumb code is dumb and it occassionally appends list to the list (list-ception)
	for card in user:
		if str(type(card)) == "<type 'list'>":
			user.remove(card)
			user.append(str(card))


	if unoDiscard[-1].split('_')[1] == 'reverse':
		unoDiscard.append(unoDiscard[-1].split('_')[0]+"_wildT")
		reverse(masterLst)
		return
	
	print 
	print "========================="
	print 'Turn for player "'+masterLst[0]+'"'
	print 'Top card is "'+unoDiscard[-1]+'"'
	print

	proceed = raw_input('Press Enter to proceed')
	if proceed == '.deck':
		for card in adminDeck:
			user.append(card)
	elif proceed == '.win':
		globals()[masterLst[0]] = []
		return

	#checks for special cases
	if unoDiscard[-1].split('_')[1] == 'drawTwo':
		for i in range(2): addCard(user, unoDiscard)
		unoDiscard.append(unoDiscard[-1].split('_')[0]+"_wildT")
		return

	try:
		if unoDiscard[-2].split('_')[1] == 'wildDraw4' and unoDiscard[-1].split('_')[1] == 'wildT':
			for i in range(4): addCard(user, unoDiscard)
			unoDiscard.append(unoDiscard[-1].split('_')[0]+"_wildT")
			return
	except:
		excpt = True


	print
	print 'Hand: ' + str(user)
	print '1. Play card and end turn'
	print '2. Draw card and end turn'
	print '3. Check hand size of next player'
	print '4. Check hand size of previous player'

	while True:
		usrInpt = raw_input("Number: ")
		try:
			usrInpt = int(usrInpt)
			if usrInpt > 5: print str(69/0)		#funny code that instintaly errors so it goes to except
			
			if usrInpt == 1:
				usrPlay = raw_input('Enter Card to Play: ')
				if usrPlay in user:		#checks to see if the player actually has the card
					
					if usrPlay.split('_')[0] == unoDiscard[-1].split('_')[0]:
						playCard(user, usrPlay)
						return
					if usrPlay.split('_')[1] == unoDiscard[-1].split('_')[1]:
						playCard(user, usrPlay)
						return
					elif usrPlay.split('_')[0] == 'wild':
						usrPlayWild = raw_input('Enter Color: ')
						if usrPlayWild.lower() not in ('blue', 'red', 'green', 'yellow'):
							print 'Not valid color'
						else:
							tempWild = usrPlayWild.lower() + '_wildT'
							playCard(user, usrPlay)
							unoDiscard.append(tempWild)
							return
				
				else:					#player does not have this card
					print "You don't have this card!"
		
			elif usrInpt == 2:
				if raw_input('Confirm [y,n]: ') == 'y':
					addCard(user, unoDiscard)
					return

			elif usrInpt == 3:
				print 'The next user, ' + masterLst[1] + ', has ' + str(len(globals()[masterLst[1]])) + ' cards left.'


			elif usrInpt == 4:
				print 'The previous user, ' + masterLst[-1] + ', has ' + str(len(globals()[masterLst[-1]])) + ' cards left.'

			else:
				print str(69/0)		#funny code that instintaly errors so it goes to except

		except:
			print 'Invalid Input'

def player(player, unoDiscard):		#have to pass unoDiscard through function because UnboundLocalError for unoDiscard

	for card in player:	#added if line because my dumb code is dumb and it occassionally appends list to the list (list-ception)
		if str(type(card)) == "<type 'list'>":
			player.remove(card)
			player.append(str(card))


	#checks for special cases on top of discard pile (i.e. needs to take an action)
	if unoDiscard[-1].split('_')[1] == 'drawTwo':
		for i in range(2): addCard(player, unoDiscard)
		unoDiscard.append(unoDiscard[-1].split('_')[0]+"_wildT")
		return
	try:
		if unoDiscard[-2].split('_')[1] == 'wildDraw4' and unoDiscard[-1].split('_')[1] == 'wildT':
			for i in range(4): addCard(player, unoDiscard)
			unoDiscard.append(unoDiscard[-1].split('_')[0]+"_wildT")
			return
	except: 
		excpt = True
	if unoDiscard[-1].split('_')[1] == 'reverse':
		reverse(masterLst)
		unoDiscard.append(unoDiscard[-1].split('_')[0]+"_wildT")
		return


	#checks if needs to use the special cases (i.e. draw cards and reverse card) first
	if int(len(globals()[masterLst[1]])) == 1:
		for card in player:
				if card.split("_")[0] == unoDiscard[-1].split("_")[0] and card.split('_')[1] == 'drawTwo':
					playCard(player, card)
					return
				if card.split("_")[0] == unoDiscard[-1].split("_")[0] and card.split('_')[1] == 'wildDraw4':
					if wild(player): 
						wild(player)
						return #checks to see if it actually played wild

				if card.split("_")[0] == unoDiscard[-1].split("_")[0] and card.split('_')[1] == 'reverse':
					playCard(player, card)
					return


	#check for color match
	for card in player:
		try:
			if card.split("_")[0] == unoDiscard[-1].split("_")[0] and card.split('_')[1] not in ('drawTwo', 'reverse'):
				playCard(player, card)
				return
		except:
			print
			print 'Error occured card is: '
			print card
			print player
			print type(card)

	#checks for number match
	for card in player:
		if card.split("_")[1] == unoDiscard[-1].split("_")[1]:
			playCard(player, card)
			return

	#checks and plays wild if necissarry
	if wild(player): 
		wild(player)
		return #checks to see if it actually played wild

	#plays the special cases without doing the calculations of the next player
	for card in player:
		if card.split("_")[0] == unoDiscard[-1].split("_")[0] and card.split('_')[1] == 'drawTwo':
			playCard(player, card)
			return
		if card.split("_")[0] == unoDiscard[-1].split("_")[0] and card.split('_')[1] == 'wildDraw4':
			if wild(player): 
				wild(player)
				return #checks to see if it actually played wild

		if card.split("_")[0] == unoDiscard[-1].split("_")[0] and card.split('_')[1] == 'reverse':
			playCard(player, card)
			return
	#last resort (draws card and ends turn)
	addCard(player, unoDiscard)
	print str([masterLst[0]]) + ' drew a card'
	#checks to see if player has no cards left


def nextPlayer():
	masterLst.append(masterLst[0])
	masterLst.pop(0)



def removeT():
	last = False
	if unoDiscard[-1].split('_')[1] == 'wildT':
		keepIndex = unoDiscard[-1]
		last = True
	for card in unoDiscard:
		try:
			if card.split('_')[1] == 'wildT':
				unoDiscard.remove(card)
		except:
			excpt = True

	if last:
		unoDiscard.append(keepIndex)



#Creates hands for players and users
for i in range(int(playerNum)):
    globals()['player_{}'.format(i)] = []
    playerLst.append('player_'+str(i))
    dealer(globals()['player_'+str(i)], handSize)

for i in range(int(userNum)):
	while True:
		userName = raw_input('Enter name of player '+str(i+1)+': ')
		if userName in usrLst:
			print 'This player already exists'
			continue
		globals()[userName] = []
		usrLst.append(userName)
		dealer(globals()[userName], handSize)
		break




#Plays Game
masterLst = usrLst+playerLst	#master lst of players
addCard(unoDiscard, unoDiscard)										#adds first card to uno discard
while unoDiscard[-1].split('_')[1] in ('wild', 'drawTwo', 'wildDraw4', 'reverse'):	#makes sure first card is not wild or a special case (draw two, reverse ect)
	unoDeck.append(unoDiscard[-1])
	unoDiscard = []
	addCard(unoDiscard, unoDiscard)


while True:
	if masterLst[0].split('_')[0] != 'player':	#if the next player is not a CPU
		user(globals()[masterLst[0]])
		for i in range(69):
			print
		checkWinner(globals()[masterLst[0]], unoDiscard)
		nextPlayer()
		removeT()
	else:
		print 'Turn of ' +masterLst[0]
		player(globals()[masterLst[0]], unoDiscard)
		checkWinner(globals()[masterLst[0]], unoDiscard)
		nextPlayer()
		removeT()