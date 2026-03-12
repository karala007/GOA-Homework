# 1. Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# def maskify(cc):
#     masked = ""
#     for i in range(len(cc)):
#         if i < len(cc) - 4:
#             masked += "#"
#         else:
#             masked += cc[i]
#     return masked


# 2. Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

#     total = 0

#     if a < b:
#         for i in range(a, b + 1):
#             total += i
#     else:
#         for i in range(b, a + 1):
#             total += i

#     return total


# 3.  An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.


# def is_isogram(string):
#     string = string.lower()
#     seen = ""

#     for letter in string:
#         if letter in seen:
#             return False
#         seen += letter

#     return True


# 4. For every good kata idea there seem to be quite a few bad ones!
# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

# def well(x):
#     good = 0

#     for i in x:
#         if i == "good":
#             good += 1

#     if good == 0:
#         return "Fail!"
#     elif good <= 2:
#         return "Publish!"
#     else:
#         return "I smell a series!"



# 5. ver gavige piroba 


# 6.   Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

# def sum_digits(number):
#     if number < 0:
#         number = -number

#     num = str(number)
    
#     total = 0
#     for i in num:
#         total += int(i)
    
#     return total


# 7. Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# def number(lines):
#     numbers = []
#     li = 1
    
#     for i in lines:

#         number = str(li) + ": " + i
#         numbers.append(number)
#         li += 1
    
#     return numbers


# 8. Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# def remove_url_anchor(url):

# return url.split("#")[0]


# 9.When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Output :: "Position of alphabet: 1"


# def position(letter):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     letter = letter.lower()

#     pos = 1 
#     for i in alphabet:
#         if i == letter:
#             return "Position of alphabet: " + str(pos)
#         pos += 1


