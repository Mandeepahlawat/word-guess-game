import re

class StringDatabase:

	def __init__(self):
		self.vocabulary = []

	def build_vocabulary(self):
		file = open('./four_letters.txt')
		lines = file.readlines()

		for line in lines:
			words_list = re.split('[^a-zA-Z]',line.lower())
			words_list = [word for word in words_list if word]
			self.vocabulary.extend(words_list)

		file.close()