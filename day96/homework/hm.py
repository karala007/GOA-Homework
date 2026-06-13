# 1)
# def spacey(array):
#     result = []
#     string = ""
    
#     for i in array:
#         string += i
#         result.append(string)
        
#     return result

# 2)

# def cube_odd(arr):
#     sum = 0
    
#     for i in arr:
#         if type(i) is bool or type(i) is not int:
#             return None

#         if i % 2 != 0:
#             value = i * i * i
#             sum += value
            
#     return sum

# 3)

# def solve(s):
#     uppercase = 0
#     lowercase = 0
#     number = 0
#     special = 0
    
#     for i in s:
#         if i.isupper():
#             uppercase += 1
#         elif i.islower():
#             lowercase += 1
#         elif i.isdigit():
#             number += 1
#         else:
#             special += 1
            
#     return [uppercase, lowercase, number, special]

# 4)


# 5)
# def solution(value):

    # values = str(value)

    # while len(values) < 5:
    #     values = "0" + values
        
    # return "Value is " + values

# 6)

# 7)
# def last_survivor(letters, coords): 

    # for i in coords:

    #     letters = letters[:i] + letters[i + 1:]
        
    # return letters

# 8)

# def solve(s):
#     maxe = 0
#     current = 0
#     vowels = "aeiou"
    
#     for i in s:
#         if i in vowels:
#             current += 1
#         else:
#             if current > maxe:
#                 maxe = current
#             current = 0

#     if current > maxe:
#         maxe = current
        
#     return maxe

# 9)
# def password(st):
#     if len(st) < 8:
#         return False
        
#     upper = False
#     lower = False
#     digit = False

#     for i in st:
#         if i.isupper():
#             upper = True
#         elif i.islower():
#             lower = True
#         elif i.isdigit():
#             digit = True

#     return upper and lower and digit

# 10)

# def is_nice(arr):
#     if len(arr) == 0:
#         return False
        
#     for i in arr:
#         neighbor = False

#         for n in arr:
#             if n == i - 1 or n == i + 1:
#                 neighbor = True
#                 break

#         if not neighbor:
#             return False
            
#     return True