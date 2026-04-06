# # 1  Your goal is to return multiplication table for number that is always an integer from 1 to 10.

# For example, a multiplication table (string) for number == 5 looks like below:

# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50
# P. S. You can use \n in string to jump to the next line.

# Note: newlines should be added between rows, but there should be no trailing newline at the end. If you're unsure about the format, look at the sample tests.

# def multi_table(number):
#     result = ""
#     for i in range(1, 11):
#         result = result + str(i) + " * " + str(number) + " = " + str(i * number)
#         if i != 10:
#             result = result + "\n"
#     return result

# ============================================================

# 2. Create a function that returns the CSV representation of a two-dimensional numeric array.

# Example:

# input:
#    [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]] 
    
# output:
#      '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'
# Array's length > 2.

# More details here: https://en.wikipedia.org/wiki/Comma-separated_values

# Note: you shouldn't escape the \n, it should work as a new line.

# def to_csv_text(array):
#     result = ""
    
#     for i in range(len(array)):
#         row = array[i]
        
#         for j in range(len(row)):
#             result += str(row[j])
            
#             if j < len(row) - 1:
#                 result += ","
        
#         if i < len(array) - 1:
#             result += "\n"
    
#     return result

# ============================================================================================


# 3. Your task is to find the first element of an array that is not consecutive.

# By not consecutive we mean not exactly 1 larger than the previous element of the array.

# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

# If the whole array is consecutive then return null2.

# The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

# 1 Can you write a solution that will return null2 for both [] and [ x ] though? (This is an empty array and one with a single number and is not tested for, but you can write your own example test. )

# 2

# Swift, Ruby and Crystal: nil
# Haskell: Nothing
# Python, Rust, Scala, Lambda Calculus: None
# Julia: nothing
# Nim: none(int) (See options)
# C++: std::nullopt

# def first_non_consecutive(arr):
#     for i in range(1, len(arr)):
#         if arr[i] - arr[i - 1] != 1:
#             return arr[i]
#     return None


# ===============================================================================================


# 4.What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.

# def add_length(str_):
#     words = str_.split()
#     result = []
#     for word in words:
#         result.append(word + " " + str(len(word)))
#     return result




# ===================================================================================================


# 5. In this kata you will create a function that takes in a list and returns a list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

# def reverse_list(l):
#     return l[::-1]

# ========================================================================================================

# 6. I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]

# NOTES:

# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that


# def human_years_cat_years_dog_years(human_years):
#     cat = 0
#     dog = 0

#     for year in range(1, human_years + 1):
#         if year == 1:
#             cat += 15
#             dog += 15
#         elif year == 2:
#             cat += 9
#             dog += 9
#         else:
#             cat += 4
#             dog += 5

#     return [human_years, cat, dog]


# ==================================================================================================

# 7.Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", 'o')  =>  1
# ("Hello", 'l')  =>  2
# ("", 'z')       =>  0
# Notes
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument will be a string of length 1

# def str_count(strng, letter):
#     count = 0
#     for char in strng:
#         if char == letter:
#             count += 1

# # 1  Your goal is to return multiplication table for number that is always an integer from 1 to 10.

# For example, a multiplication table (string) for number == 5 looks like below:

# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50
# P. S. You can use \n in string to jump to the next line.

# Note: newlines should be added between rows, but there should be no trailing newline at the end. If you're unsure about the format, look at the sample tests.

# def multi_table(number):
#     result = ""
#     for i in range(1, 11):
#         result = result + str(i) + " * " + str(number) + " = " + str(i * number)
#         if i != 10:
#             result = result + "\n"
#     return result

# ============================================================

# 2. Create a function that returns the CSV representation of a two-dimensional numeric array.

# Example:

# input:
#    [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]] 
    
# output:
#      '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'
# Array's length > 2.

# More details here: https://en.wikipedia.org/wiki/Comma-separated_values

# Note: you shouldn't escape the \n, it should work as a new line.

# def to_csv_text(array):
#     result = ""
    
#     for i in range(len(array)):
#         row = array[i]
        
#         for j in range(len(row)):
#             result += str(row[j])
            
#             if j < len(row) - 1:
#                 result += ","
        
#         if i < len(array) - 1:
#             result += "\n"
    
#     return result

# ============================================================================================


# 3. Your task is to find the first element of an array that is not consecutive.

# By not consecutive we mean not exactly 1 larger than the previous element of the array.

# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

# If the whole array is consecutive then return null2.

# The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

# 1 Can you write a solution that will return null2 for both [] and [ x ] though? (This is an empty array and one with a single number and is not tested for, but you can write your own example test. )

# 2

# Swift, Ruby and Crystal: nil
# Haskell: Nothing
# Python, Rust, Scala, Lambda Calculus: None
# Julia: nothing
# Nim: none(int) (See options)
# C++: std::nullopt

# def first_non_consecutive(arr):
#     for i in range(1, len(arr)):
#         if arr[i] - arr[i - 1] != 1:
#             return arr[i]
#     return None


# ===============================================================================================


# 4.What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.

# def add_length(str_):
#     words = str_.split()
#     result = []
#     for word in words:
#         result.append(word + " " + str(len(word)))
#     return result




# ===================================================================================================


# 5. In this kata you will create a function that takes in a list and returns a list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

# def reverse_list(l):
#     return l[::-1]

# ========================================================================================================

# 6. I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]

# NOTES:

# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that


# def human_years_cat_years_dog_years(human_years):
#     cat = 0
#     dog = 0

#     for year in range(1, human_years + 1):
#         if year == 1:
#             cat += 15
#             dog += 15
#         elif year == 2:
#             cat += 9
#             dog += 9
#         else:
#             cat += 4
#             dog += 5

#     return [human_years, cat, dog]


# ==================================================================================================

# 7.Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", 'o')  =>  1
# ("Hello", 'l')  =>  2
# ("", 'z')       =>  0
# Notes
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument will be a string of length 1

# def str_count(strng, letter):
#     count = 0
#     for char in strng:
#         if char == letter:
#             count += 1
#     return count