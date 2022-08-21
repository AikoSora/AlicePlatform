from difflib import SequenceMatcher
from math import floor


def search_matches(words, text):
    """Function for searching for similar words in a string"""
    
    assert len(words) > 0, "Empty list!"
    assert text, "Empty string!"

    matches_number = 0

    for word in text.split():

        for command in words:

            string_one = word.lower()
            string_two = command.lower()

            matcher = SequenceMatcher(None, string_one, string_two)

            if matcher.ratio() > 0.8:
                matches_number += 1
                break

    if matches_number >= len(words):
        return True
    return False
