from string import ascii_lowercase as alc
from typing import Dict
import re


def SortDictionary(aDict: Dict[str, int]):
    sortedDict = [(k, v)
                  for k, v in sorted(aDict.items(), key=lambda item: -item[1])]
    return sortedDict


def InitAlphabetDict() -> Dict[str, int]:
    alphabetDict = dict()
    for letter in alc:
        alphabetDict[letter] = 0
    return alphabetDict


def CountWordsInString(aString: str) -> int:
    words = aString.split()
    return len(words)


def GetLetterHistogram(text: str) -> Dict[str, int]:
    bins = InitAlphabetDict()

    for letter in text:
        # print(letter)
        letter = letter.lower()
        if letter in alc:
            bins[letter] = bins[letter] + 1

    return bins


def DisplayStatistics(book_path: str, num_words: int, letter_bins: str):
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document]\n")

    sorted_dict = SortDictionary(letter_bins)
    for item in sorted_dict:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print(f"--- End report ---")


if __name__ == '__main__':
    book_path = "books/frankenstein.txt"
    with open(book_path, "r") as book:
        book_read = book.read()
        word_count = CountWordsInString(book_read)

        letter_frequencies = GetLetterHistogram(book_read)
        print(letter_frequencies)

        DisplayStatistics(book_path=book_path,
                          num_words=word_count, letter_bins=letter_frequencies)
