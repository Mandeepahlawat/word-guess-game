class Game:
	"""
	This class stores all the information related to the individual and overall game.
	It contains all the methods like guess_letter, guess_word, tell_word which are used to play the game.
	It also contains some helper functions to print the summary and to calculate the score.
	"""

	LETTER_WITH_FREQUENCIES = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09,
		'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33,
		't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07
	}

	
	def __init__(self):
		"""
		This is the constructor of the Game class and initializes all the variables
		which contains information about the game.
		"""
		self.guessed_word_count = 0
		self.current_guess = '----'
		self.total_stats = []
		self.current_bad_guesses = 0
		self.current_missed_letters = 0
		self.current_score = 0
		self.current_status = 'success'
		self.letter_request_count = 0

	def reset_current_game_values(self):
		"""
		This is a helper method which is used to reset all the variables once a individual game
		is finished and a new game starts, by resetting them to initial values we can keep using
		these variables to maintain the individual game statistics
		"""
		self.current_guess = '----'
		self.guessed_word_count = 0
		self.current_bad_guesses = 0
		self.current_missed_letters = 0
		self.current_score = 0
		self.letter_request_count = 0

	def guess_letter(self):
		"""
		This method is called when user selects the option to guess a individual letter.
		It checks if user has guessed a correct letter, if not it displays the wrong letter
		message and increments the missed letter count
		"""
		guessed_letter = input("Enter a letter:\n")
		self.letter_request_count += 1

		while(len(guessed_letter) != 1):
			print("Incorrect!! You can only enter 1 letter")
			guessed_letter = input("Enter a letter:\n")
		
		if guessed_letter in self.current_letters_to_guess:
			guessed_letter_pos = [pos for pos, char in enumerate(self.current_word) if char == guessed_letter]
			self.guessed_word_count += len(guessed_letter_pos)

			self.current_letters_to_guess = list(filter(lambda a: a != guessed_letter, self.current_letters_to_guess))
			
			print("You found %s letter" % len(guessed_letter_pos))
			
			self.current_guess = list(self.current_guess)
			
			for pos in guessed_letter_pos:
				self.current_guess[pos] = guessed_letter
			self.current_guess = ''.join(self.current_guess)
		else:
			print("Wrong choice of letter")
			self.current_missed_letters += 1

	def guess_last_letter(self):
		"""
		This method is called when user selects the option to guess a individual letter and only
		a single letter is remaining is left, so it behaves like guessing the whole word
		"""
		guessed_letter = input("Enter a letter:\n")
		self.letter_request_count += 1

		while(len(guessed_letter) != 1):
			print("Incorrect!! You can only enter 1 letter")
			guessed_letter = input("Enter a letter:\n")

		if guessed_letter in self.current_letters_to_guess:
			print("Voila!! You found correct word!")
			self.guessed_word_count = len(self.current_word)
			if self.letter_request_count != 0:
				self.current_score += (self.get_current_score()/self.letter_request_count)
			else:
				self.current_score += (self.get_current_score())
		else:
			print("Wrong choice of letter")
			self.current_missed_letters += 1

	def guess_word(self):
		"""
		This method is called when user selects the option to guess the full word.
		It checks if the word is correctly guessed increaese the score, if not it 
		increments the bad guess count and decreases the score.
		"""
		guessed_word = input("Enter word:\n")

		while(len(guessed_word) != len(self.current_word)):
			print("Incorrect!! All words are of 4 characters\n")
			guessed_word = input("Enter word:\n")
		
		if guessed_word == self.current_word:
			print("Voila!! You found correct word!")
			self.guessed_word_count = len(self.current_word)
			
			if self.letter_request_count != 0:
				self.current_score += (self.get_current_score()/self.letter_request_count)
			else:
				self.current_score += (self.get_current_score())
		else:
			print("Wrong word!!")
			self.current_bad_guesses += 1
			self.current_score -= (self.get_current_score(True) * 0.10)

	def tell_word(self):
		"""
		This method is called when user selects the option to give up and
		wants to know the correct word, It decreases the total score by
		number of letters that were not guessed during that time
		"""
		self.current_status = 'Gave up'
		print("Correct word is %s\n" % self.current_word)
		self.guessed_word_count = len(self.current_word)
		self.current_score -= self.get_current_score()

	def print_game_stats(self):
		"""
		This is a helper method is used to print the overall game summary on
		console, with overall score and individual game stats
		"""
		print("\n\n\nGame Summary:")
		print("===========================================\n")
		print('{:<10}{:<10}{:<20}{:<20}{:<20}{:<20}'.format('Game', 'Word', 'Status', 'Bad Guesses', 'Missed Letters', 'Score'))
		print('{:<10}{:<10}{:<20}{:<20}{:<20}{:<20}'.format('-----', '-----','-----', '-----','-----', '-----'))
		total_score = 0
		for index, stat in enumerate(self.total_stats):
			total_score += stat['score']
			print('{:<10}{:<10}{:<20}{:<20}{:<20}{:<20.2f}'.format(index+1, stat['word'], stat['status'], stat['bad_guesses'], stat['missed_letters'], stat['score']))
		print("\n\n Final Score: %.2f"%total_score)
		print("\n===========================================")

	def get_current_score(self, is_total=False):
		"""
		This is a helper method to calculate the score for a particular word.
		If is_total is true then it calculates the total score for current word
		otherwise it calculates the score for letters which are not yet guessed
		by the user.

		@param is_total - A boolean value indicating if we want to calculate
		total score for current word
		"""
		word_list = list(self.current_word)
		score = 0
		for letter in word_list:
			score += Game.LETTER_WITH_FREQUENCIES[letter.lower()]
		
		if not is_total:
			curent_guess_list = list(self.current_guess)
			for letter in curent_guess_list:
				if letter != '-':
					score -= Game.LETTER_WITH_FREQUENCIES[letter.lower()]

		return score
