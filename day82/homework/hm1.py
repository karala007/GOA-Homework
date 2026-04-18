# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# def spin_words(sentence):
#     words = sentence.split()
#     result = ""

#     for i in range(len(words)):
#         word = words[i]

#         if len(word) >= 5:
#             word = word[::-1]

#         result += word

#         if i != len(words) - 1:
#             result += " "

#     return result

# =====================================================================

# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

# Good luck!

# def capitalize(s):    
#     even = ""
#     odd = ""

#     for i in range(len(s)):
#         if i % 2 == 0:
#             even += s[i].upper()
#             odd += s[i]
#         else:
#             even += s[i]
#             odd += s[i].upper()

#     return [even, odd]

# =================================================================================

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# def reverse_words(text):
#     words = text.split(" ")
#     result = ""

#     for i in range(len(words)):
#         result += words[i][::-1]
#         if i != len(words) - 1:
#             result += " "

#     return result


# ==================================================================================

# We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

# So given a string "super", we should return a list of [2, 4].

# Some examples:
# Mmmm  => []
# Super => [2,4]
# Apple => [1,5]
# YoMama -> [1,2,4,6]
# NOTES
# Vowels in this context refers to: a e i o u y (including upper case)
# This is indexed from [1..n] (not zero indexed!)

# def vowel_indices(word):
#     vowels = "aeiouyAEIOUY"
#     result = []

#     for i in range(len(word)):
#         if word[i] in vowels:
#             result.append(i + 1)

#     return result


# =============================================================================================

