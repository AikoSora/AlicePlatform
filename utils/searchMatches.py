from difflib import SequenceMatcher
from math import floor


def searchMatches(words, text):
	"""Function for searching for similar words in a string"""
	assert len(words) > 0, "Empty list!"
	assert text, "Empty string!"

	matchesNumber = 0

	for word in text.split():

		for command in words:

			stringOne = word.lower()
			stringTwo = command.lower()

			matcher = SequenceMatcher(None, stringOne, stringTwo)

			if matcher.ratio() > 0.8:
				matchesNumber += 1
				break

	if matchesNumber >= len(words):
		return True
	return False