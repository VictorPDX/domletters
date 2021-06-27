#!/usr/bin/env

import re
import sys
import collections
from string import punctuation


def count_domLetters(word):
    """The acutal algorithm that does the counting of the dominant letters in the input.

    Args:
        word ([type]): The word whose dominant letters are being counted.

    Returns:
        [int]: Returns the frequency of the dominant letter.
    """
    # https://stackoverflow.com/questions/4131123/finding-the-most-frequent-character-in-a-string
    # count the letters in the word returning the most common letter and frequency
    domletter, freq = collections.Counter(word.lower()).most_common(1)[0]

    print(word.ljust(15), end="\t")
    print(f"{domletter: <2} appeared {freq} times", end="\t")
    return freq


def domLetters(list_of_words):
    """This function takes in a list containing all the tokens from the input.
        It will look for'alphabetical words' and find the dominant letter.
        It tallies the count of all the dominant letters in the list.

    Args:
        list_of_words (list): The input text whose dominant letters will be counted.

    Returns:
        [int]: The sum of dominant letter from the current list of words.
    """
    sum = 0
    # loop over all the word in the input file
    for token in list_of_words:
        # we ignore any tokens that are not considered words
        if not any(punc in token for punc in punctuation):
            sum += count_domLetters(token)
            print(f"Sum: {sum}")
    return sum

if __name__ == "__main__":
    sum = 0
    # if input if provided as a text file
    if len(sys.argv) > 1 and sys.argv[1].endswith(".txt"):
        fname = sys.argv[1]
        fileObject = open(fname, "rt")
        list_of_words = fileObject.read().split()
        sum = domLetters(list_of_words)
    else:
        # if input if provided via io stdin
        for line in sys.stdin:
            list_of_words = line.split()

            # pass in the list to the dominant letters function
            sum += domLetters(list_of_words)
    print(f"Sum: {sum}")

else:
    print("This is a script and not a module. Do not import.")