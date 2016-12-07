#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_pyreview` -- Python review
=========================================

LAB PyReview Learning Objective: Review the topics from the previous courses

a. Load the data from the two dictionary files in the data directory into two
   list objects.  data/dictionary1.txt data/dictionary2.txt
   Print the number of entries in each list of words.

b. Use sets in Python to merge the two lists of words with no duplications (union).
   Print the number of words in the combined list.

c. Import the random library and use one of the functions to print out five random
   words from the combined list of words.

d. Use a list comprehension to find all the words that start with the letter 'a'.
   Print the number of words that begin with the letter 'a'.

e. Create a function called wordcount() with a yield that takes the list of
   all words as an argument and yields a tuple of
   (letter, number_of_words_starting_with_that_letter) with each iteration.

"""
import random
import string


# helper functions
def strip_newlines(list_of_words):
    return [l.strip() for l in list_of_words]


# step a.
print("step a.")
with open("../data/dictionary1.txt", "r") as d1:
    raw_dictionary1 = d1.readlines()
dictionary1 = strip_newlines(raw_dictionary1)
print(('Number of entries in dictionary1: {}'.format(len(dictionary1))))

raw_dictionary2 = open("../data/dictionary2.txt", "r").readlines()
dictionary2 = strip_newlines(raw_dictionary2)
print(('Number of entries in dictionary2: {}'.format(len(dictionary2))))
print('')

# step b.
print("step b.")
sd1 = set(dictionary1)
sd2 = set(dictionary2)
scombined = sd1.union(sd2)
dictionary_combined = list(scombined)
print(('Number of entries in combined dictionaries: {}'.format(len(dictionary_combined))))
print('')

# step c.
print("step c.")
for i in range(5):
    word = random.choice(dictionary_combined)
    print(("Word {}: {}".format(i+1, word)))
print('')

# alternate step c.:
print("alternate step c.")
words = random.sample(dictionary_combined, 5)
for (i, word) in enumerate(words):
    print(("Word {}: {}".format(i+1, word)))
print('')

# step d.
print('step d.')
awords = [w for w in dictionary_combined if w.startswith('a')]
print(("Number of words starting with 'a': {}".format(len(awords))))
print('')


# step e.
def wordcount(wordlist):
    for letter in string.ascii_lowercase:
        words = [w for w in wordlist if w.startswith(letter)]
        yield (letter, len(words))


print('step e.')
for wc in wordcount(dictionary_combined):
    print(("Number of words starting with {}: {}".format(wc[0], wc[1])))
print('')
