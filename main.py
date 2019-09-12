# Leave this to import things.
import random


# Black Jack

def blackjack():
	def user_commands():
		if user_input == "deal":
			deal_cards()
		elif user_input == "rules":
			print('Welcome to blackjack!\nRules are simple, in this version the dealer will always stay on two cards.\n You of course can hit as much as you need')
		elif user_input == "hit":
			hit()
		elif user_input == "stay":
			print('You choose to stay')
		pass

	

	def deal_cards():
		

		playing_cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
		dealer_hand = []
		player_hand = []
		dealer_total_cards = 0
		player_total_cards = 0
		user_is_active = True
		user_not_bust = True

		def hit():
			i = random.randint(0,len(playing_cards))
			player_hand.append(playing_cards[i])
			playing_cards.pop(i)

		def convert_face_cards(i, playing_cards):
			#if a face card was put into a player's inventory convert it to an int
			pass
			

		## Dealers hand dealing
		while dealer_total_cards < 2:
			i = random.randint(0,len(playing_cards))
			dealer_hand.append(playing_cards[i])
			playing_cards.pop(i)
			dealer_total_cards += 1
			print(dealer_hand)

		## Players Hand Deal
		while player_total_cards < 2:
			i = random.randint(0,len(playing_cards))
			player_hand.append(playing_cards[i])
			playing_cards.pop(i)
			player_total_cards += 1

		print(playing_cards)


		#while user_is_active:
		print(f'You have {player_hand} in your hand\n The sum of which is: {sum(player_hand)}')
		while user_not_bust:
			if sum(player_hand) <= 21:
				user_input = input("What do you want to do? Hit or Stay: ")
				if user_input == 'hit':
					hit()
					print(f'You have: {player_hand}')
				elif user_input == 'stay':
					break

		
		








			

	deal_cards()

	print('The cards have been dealt')

	





# Coin Flip Game
def coin_game():
	user_choice = input('Choose heads or tails: ')
	user_total_points = 50
	user_bet = int(input(f'You have {user_total_points} coins available\n How much would you like to bet?: '))
	if user_bet > user_total_points:
		print('Sorry you cannot bet more than you have please enter another amount')


	def coin_flip(choice, points):
		rand_int = random.randint(0,2)

		if rand_int == 0 and user_choice == 'tails':
			print(f'The coin flipped was: Tails\nYou selected {user_choice}')
			result = 'Victory'
		elif rand_int == 1 and user_choice == 'heads':
			print(f'The coin flipped was: Heads\nYou selected {user_choice}')
			result = 'Victory'
		else:
			result = 'Loss'

		return result




	victory = coin_flip(user_choice, user_total_points)
	print('Result: ' + victory)


## write a few betters games
def main():
	no_game = True
	## indicate what games you want to play or instructions to call.
	while no_game:
		play_options = input('what do you want to play: ')
		if play_options == 'blackjack':
			blackjack()
			break
		else:
			print('please enter from the list of games')
	pass

main()
