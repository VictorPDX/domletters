#!/usr/bin/env python3

import re
import collections
from string import punctuation


def count_domLetters(fname="sentence.txt"):
    """This function takes in an input looking for
        'alphabetical words' and finding the dominant letter.
        It tallies the count of dominant letters in the input.

    Args:
        fname (str, optional): The input text whose dominant letters will be counted. Defaults to "sentence.txt".
    """
    fileObject = open(fname, "rt")
    list_of_words = fileObject.read().split()
    sum = 0

    # loop over all the word in the input file
    for token in list_of_words:
        # we ignore any tokens that are not considered words
        if not any(punc in token for punc in punctuation):
            # https://stackoverflow.com/questions/4131123/finding-the-most-frequent-character-in-a-string
            # count the letters in the word returning the most common letter and frequency
            domletter, freq = collections.Counter(token.lower()).most_common(1)[0]
            sum += freq

            print(token.ljust(15), end="\t")
            print(f"{domletter: <2} appeared {freq} times", end="\t")
            print(f"Sum: {sum}")


if __name__ == "__main__":
    fname = "swift.txt"
    # count_domLetters(fname)
    count_domLetters()
else:
    print("This is a script and not a module. Do not import.")