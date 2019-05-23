import re

class StringDatabase:
	"""
	This class is responsible for disk I/O operation and
	reads the contents of a file and builds the vocabulary
	from which game class randomly selects a word.
	"""

	def __init__(self):
		"""
		This is the constructor for StringDatabase class and
		initializes the vocabulary variable, which is a list
		of the all available words
		"""
		self.vocabulary = []

	def build_vocabulary(self):
		"""
		This method reads the file containing all the words
		and then populates the vocabulary list.
		"""
		file = open('./four_letters.txt')
		lines = file.readlines()

		for line in lines:
			words_list = re.split('[^a-zA-Z]',line.lower())
			words_list = [word for word in words_list if word]
			self.vocabulary.extend(words_list)

		file.close()