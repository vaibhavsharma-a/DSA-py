
#! not optimal way of doing the hashing
# arr = [1,2,2,3,4,5,3,3,2,3,5]
# size = len(arr)

# ans_list = []
# def return_count(number, arr):
#   count = 0
#   for i in range(0,size):
#     if number == arr[i]:
#       count +=1
#   ans_list.append(count)

#   return count

# query = [1,2,3,4,5]


# for num in query:
#   return_count(num,arr)

# print(ans_list)

#! Optimized way of doing the hashing

# arry = [1,2,3,4,5,4,5,5,3,5,5,6,7,8,9,7,9,6,4,7,8,9]

# # size_of_arr = len(arry)

# hased_arr = [0]*len(arry)

# # print(zeros_arr)
# #! creating the hased array based on the given arr
# for number in arry:
#   hased_arr[number] +=1
# # print(hased_arr)

# #! to fetch the occurance of a particular element present in the array
  
# elem_arr = int(input("Enter the number whose occurance to be found\n"))

# print(f"The occurance of the element {elem_arr} is {hased_arr[elem_arr]} times in the main array")

#! for the characters
#? Brute force

# string = "abdbgbcbcbcbebcb"
# n = len(string)
# def find_occur_char(char, string:str):
#   cnt = 0
#   for i in range(0,n):
#     if (string[i] == char):
#       cnt += 1
#   return cnt

# print(find_occur_char("b",string))

#! better way of doing it with hashes (if containing only lowercase letters)

# string = "hellowiamvaibhavandiamfromludhianapunajbandiwilldomybesttodogoodstuffinlife"

# hashed_chars = [0]*26

# # prestoring the valued hash
# for char in string:
#   hashed_chars[ord(char) - ord("a")] += 1

# # print(hashed_chars)
  
# find_char = input("Enter the char you want to find the occcurance of\n")

# print(f"The character {find_char} is present {hashed_chars[ord(find_char)-ord("a")]} times in the string")

#? for all type of char present

# string = "My anADF jiaf ADFADF fadfafad AADFadfadfFADF AFSDF"

# hashed_chars = [0]*256

# # prestoring the valued hash
# for char in string:
#   hashed_chars[ord(char)] += 1

# # print(hashed_chars)
  
# find_char = input("Enter the char you want to find the occcurance of\n")

# print(f"The character {find_char} is present {hashed_chars[ord(find_char)]} times in the string")