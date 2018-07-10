#import stuff
import sys
import random
#create wins variables
wins1 = 0
wins2 = 0
#creates interested variable and starts megaloop
interested = 1
while interested == 1:
	#make the deck
	print "\nYou: ------------- %s wins"%(wins1)
	print "Your apponent: --- %s wins"%(wins2)
	gameon = 0
	deck = (range(52))
	print deck
	names = ["Ace of spades","Ace of hearts","Ace of diamonds","Ace of clubs","King of spades","King of hearts","King of diamonds","King of clubs","Queen of spades","Queen of hearts","Queen of diamonds","Queen of clubs","Jack of spades","Jack of hearts","Jack of diamonds","Jack of clubs","10 of spades","10 of hearts","10 of diamonds","10 of clubs","9 of spades","9 of hearts","9 of diamonds","9 of clubs","8 of spades","8 of hearts","8 of diamonds","8 of clubs","7 of spades","7 of hearts","7 of diamonds","7 of clubs","6 of spades","6 of hearts","6 of diamonds","6 of clubs","5 of spades","5 of hearts","5 of diamonds","5 of clubs","4 of spades","4 of hearts","4 of diamonds","4 of clubs","3 of spades","3 of hearts","3 of diamonds","3 of clubs","2 of spades","2 of hearts","2 of diamonds","2 of clubs"]
	#shuffle
	transition = 0
	for shufflecount in range(100):
		a, b = random.randint (0,51), random.randint (0,51)
		deck[b], deck[a] = deck[a], deck[b]
	print deck
	#deal
	deck1 = deck [0:26]
	deck2 = deck [26:52]
	print deck1
	print deck2
	#setup notice
	print "Game setup complete!",
	#main game loop
	gameon = 1
	turn = 1
	war = 0
	army1 = []
	army2 = []
	while gameon == 1:
		raw_input ("Turn %s | Press enter to play a card:"%(turn))
		print ""
		card1 = deck1[0]
		card2 = deck2[0]
		print "You played the %s"%(names[card1])
		print "Your opponent played the %s"%(names[card2])
		#if you win:
		if (card1 // 4) < (card2 // 4):
			print "You win!"
			deck1.remove (card1)
			deck2.remove (card2)
			deck1.append (card1)
			deck1.append (card2)
			##print "you: %s"%(deck1)
			##print "AI: %s"%(deck2)
			print "Your deck: -------------- %s cards"%(len (deck1))
			print "Your apponent's deck: --- %s cards"%(len (deck2))
			print ""
		else:
			#if you lose
			if (card1 // 4) > (card2 // 4):
				print "You lose."
				deck1.remove (card1)
				deck2.remove (card2)
				deck2.append (card1)
				deck2.append (card2)
				##print "you: %s"%(deck1)
				##print "AI: %s"%(deck2)
				print "Your deck: -------------- %s cards"%(len (deck1))
				print "Your apponent's deck: --- %s cards"%(len (deck2))
				print ""
			else:
				#WAR!
				war = 1
				while war == 1:
					print "War!"
					print ""
					if card1 in deck1:
						deck1.remove (card1)
					if card2 in deck2:
						deck2.remove (card2)
					#check if you win or lose the game
					if len (deck1) <= 5:
						print "You lost the entire game after %s turns..."%(turn)
						wins2+=1
						print "Thanks for playing!"
						gameon = 0
						break
					if len (deck2) <= 5:
						print "You won the entire game in %s turns!"%(turn)
						wins1+=1
						print "Thanks for playing!"
						gameon = 0
						break
					#build army
					army1.append (card1)
					army1.append (deck1[0])
					army1.append (deck1[1])
					army1.append (deck1[2])
					card1 = deck1[3]
					army2.append (card2)
					army2.append (deck2[0])
					army2.append (deck2[1])
					army2.append (deck2[2])
					card2 = deck2[3]
					#remove army cards from deck
					deck1.remove (card1)
					deck1.remove (deck1[0])
					deck1.remove (deck1[1])
					deck1.remove (deck1[2])
					deck2.remove (card2)
					deck2.remove (deck2[0])
					deck2.remove (deck2[1])
					deck2.remove (deck2[2])
					#print stuff
					##print "Your army: %s"%(army1)
					print "You have and your apponent have %s cards face down"%(len (army1))
					print ""
					print "You played the %s"%(names[card1])
					##print "Your apponent's army: %s"%(army2)
					print "Your aponnent played the %s"%(names[card2])
					#if you win
					if (card1 // 4) > (card2 // 4):
						print "You lose."
						##deck2.append (army1)
						##deck2.append (army2)
						deck2 = deck2 + army2
						deck2 = deck2 + army1
						deck2.append (card2)
						deck2.append (card1)
						##print "you: %s"%(deck1)
						##print "AI: %s"%(deck2)
						print "Your deck: -------------- %s cards"%(len (deck1))
						print "Your apponent's deck: --- %s cards"%(len (deck2))
						army1 = []
						army2 = []
						print ""
						war = 0
					else:
						#if you lose
						if (card1 // 4) < (card2 // 4):
							print "You win!"
							##deck1.append (army1)
							##deck1.append (army2)
							deck1 = deck1 + army1
							deck1 = deck1 + army2
							deck1.append (card1)
							deck1.append (card2)
							##print "you: %s"%(deck1)
							##print "AI: %s"%(deck2)
							print "Your deck: -------------- %s cards"%(len (deck1))
							print "Your apponent's deck: --- %s cards"%(len (deck2))
							army1 = []
							army2 = []
							print ""
							war = 0
		#if you lose the game
		if deck1 == []:
			print "You lost the entire game after %s turns..."%(turn)
			print "Thanks for playing!"
			wins2+=1
			gameon = 0
			break
		else:
			#if you win the game
			if deck2 == []:
				print "You won the entire game in %s turns!"%(turn)
				print "Thanks for playing!"
				wins1+=1
				gameon = 0
				break
			else:
				turn+=1
	exited = ""
	while exited == "":
		exited = raw_input ("Do you want to play again? [Y/n] ")
		print '\033[1A',
	if exited == "y" or "Y":
		interested = 1
	if exited == "n" or "N":
		interested = 0
		sys.exit("\nGoodbye...")