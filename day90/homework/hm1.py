# 1-
# def reverse_number(n):
#     negative = n < 0
    
#     if negative:
#         n = n * -1
        
#     num1 = str(n)
#     reversed_str = ""
    
#     for i in num1:
#         reversed_str = i + reversed_str
        
#     reversed_num = int(reversed_str)
    
#     if negative:
#         return -reversed_num
#     else:
#         return reversed_num

# 2-
# def most_frequent_item_count(collection):
#     if not collection:
#         return 0
        
#     max_count = 0
    
#     for i in collection:
#         count = collection.count(i)
#         if count > max_count:
#             max_count = count
            
#     return max_count

# 3-
# def has_unique_chars(string):
#     seen = []
    
#     for i in string:
#         if i in seen:
#             return False
#         seen.append(i)
        
#     return True

# 4-
# def flatten(lst):
#     result = []
    
#     for i in lst:
#         if type(i) is list:
#             for sum in i:
#                 result.append(sum)
#         else:
#             result.append(i)
            
#     return result

# 5-
# def sum_of_integers_in_string(s):
#     sum = 0
#     current = ""
    
#     for i in s:
#         if i.isdigit():
#             current = current + i
#         else:
#             if current:
#                 sum = sum + int(current)
#                 current = ""
                
#     if current:
#         sum =sum + int(current)
        
#     return sum

# 6-
# def pairs(arr):
#     count = 0
    
#     for i in range(0, len(arr) - 1, 2):
#         if arr[i] -1 == arr[i+1] or arr[i+1] -1 == arr[i]:
#             count += 1
            
#     return count