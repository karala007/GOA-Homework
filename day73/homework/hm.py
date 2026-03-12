# 1. Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database. At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.

# def string_clean(s):

#     result = ""
    
#     for ch in s:
#         if not ch.isdigit():
#             result += ch
            
#     return result

# 2. You need to write a function that reverses the words in a given string. Words are always separated by a single space.

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace

# def reverse(st):
#     words = st.split()
#     result = ""

#     for i in range(len(words) - 1, -1, -1):
#         result += words[i]
#         if i != 0:
#             result += " "

#     return result

# 3.This is a beginner friendly kata especially for UFC/MMA fans.

# It's a fight between the two legends: Conor McGregor vs George Saint Pierre in Madison Square Garden. Only one fighter will remain standing, and after the fight in an interview with Joe Rogan the winner will make his legendary statement. It's your job to return the right statement depending on the winner!

# If the winner is George Saint Pierre he will obviously say:

# "I am not impressed by your performance."
# If the winner is Conor McGregor he will most undoubtedly say:

# "I'd like to take this chance to apologize.. To absolutely NOBODY!"
# Good Luck!

# Note
# The given name may varies in casing, eg., it can be "George Saint Pierre" or "geOrGe saiNT pieRRE". Your solution should treat both as the same thing (case-insensitive).

# def quote(fighter):

#     if fighter.lower() == "george saint pierre":
#         return "I am not impressed by your performance."
#     else:
#         return "I'd like to take this chance to apologize.. To absolutely NOBODY!"

# 4.ver gavige


# 5.write me a function stringy that takes a size and returns a string of alternating 1s and 0s.

# the string should start with a 1.

# a string with size 6 should return :'101010'.

# with size 4 should return : '1010'.

# with size 12 should return : '101010101010'.

# The size will always be positive and will only use whole numbers.
# ---
# def stringy(size):
#     result = ""
    
#     for i in range(size):
#         if i % 2 == 0:
#             result = result + "1"
#         else:
#             result = result + "0"
            
#     return result
