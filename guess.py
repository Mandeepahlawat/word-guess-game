from stringDatabase import StringDatabase
from game import Game
import random

class Guess:

	def __init__(self):
		stringDatabase = StringDatabase()
		stringDatabase.build_vocabulary()
		game = Game()

		print("** The great guessing game **")
		game_count = 1
		
		while game_count <= 100:
			game.current_word = random.choice(stringDatabase.vocabulary)
			game.current_letters_to_guess = list(game.current_word)
			print("%s\n" % game.current_word)

			user_input = None

			while(game.guessed_word_count != len(game.current_word)):
				print("Current Guess: %s" % game.current_guess)
				if game.guessed_word_count == len(game.current_word) - 1:
					user_input = input("g = guess, t = tell me and q to quit\n")
					while user_input not in ["g", "t", "q"]:
						print("Incorrect option!!\n")
						user_input = input("g = guess, t = tell me and q to quit\n")
				else:
					user_input = input("g = guess, t = tell me, l for a letter, and q to quit\n")
					while user_input not in ["g", "t", "l", "q"]:
						print("Incorrect option!!\n")
						user_input = input("g = guess, t = tell me, l for a letter, and q to quit\n")
				
				if user_input == 'g':
					game.guess_word()
				elif user_input == 't':
					game.tell_word()
				elif user_input == 'l':
					game.guess_letter()
				elif user_input == 'q':
					game_count = 100
					break;

			if user_input != 'q':
				game.total_stats.append(
					{
						'word': game.current_word, 
						'status': game.current_status, 
						'bad_guesses': game.current_bad_guesses, 
						'missed_letters': game.current_missed_letters, 
						'score': game.current_score
					}
				)
			game_count += 1
			game.reset_current_game_values()

		game.print_game_stats()

guess = Guess()