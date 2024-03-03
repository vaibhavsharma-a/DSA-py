# def print_for_n_to_1(number):
#   if number == 1:
#     print(number)
#   else:
#     print(number)
#     print_for_n_to_1(number - 1)

# number = int(input("Enter the number \n"))

# print_for_n_to_1(number)

# def print_one_to_n(i,num):
#   if i>num:
#     return
#   else:
#     print(i)
#     print_one_to_n(i+1,num)

# number = int(input("Enter the number \n"))
# print_one_to_n(1,number)

# def print_name_times(name,n):
#   if n == 1:
#     print(name)
#   else:
#     print(name)
#     print_name_times(name,n-1)
    
# name = input("Enter the name you want to print\n")
# number = int(input("Enter the number of times you want to print\n"))

# print_name_times(name,number)

#! recursion using back tracking

# def backtrack_one_to_num(i,num):
#   if (i<1):
#     return
#   else:
#     backtrack_one_to_num(i-1,num)
#     print(i)

# number = int(input("Enter a number to be printed\n"))
# backtrack_one_to_num(number,number)
# print("-----------------------------------")
# #! another back track from the number n to number 1 print
# #? if num = 3 then print in the fashion like 3,2,1

# def backtrack_num_to_one(i,num):
#   if (i>num):
#     return
#   else:
#     backtrack_num_to_one(i+1,num)
#     print(i)

# number = int(input("Enter a number to be printed\n"))
# backtrack_num_to_one(1,number)

#! sum of n number using recursion

# def sum_of_n_number(number) -> int:
#   if number == 0:
#     return 0
#   else:
#     return number + sum_of_n_number(number - 1)

# total = sum_of_n_number(5)
# print(total)

# def pram_sum_of_n(i,sum):
#   if i < 0:
#     print(sum)
#     return
#   else:
#     pram_sum_of_n(i-1,sum+i)

# number = int(input("Enter the number\n"))
# pram_sum_of_n(number,0)

#! factorial of n number

# def facto(number):
#   if number == 1 or number == 0:
#     return 1
#   else:
#     return number * facto(number-1)
  
# fact_of_five = facto(5)
# print(fact_of_five)

# def pram_fact_of_n(i,prod):
#   if i==0 or i==1:
#     print(prod)
#   else:
#     pram_fact_of_n(i-1,prod*i)

# pram_fact_of_n(1,1)

#! reversing the array/list using recursion 
#? doing with the two pointer

# array_list = []
# number = int(input("Enter the number as the size of the array\n"))

# for i in range(0,number):
#   elem = input(f"Enter the elemnet at {i}th index of the array\n")
#   array_list.append(elem)

# print(array_list)


# left = 0
# right = number - 1

# def reverse_an_array(arr:list,left:int,right:int) -> list:
#   if left >= right:
#     return
#   else:
#     array_list[left],array_list[right] = array_list[right],array_list[left]
#     reverse_an_array(arr,left+1,right-1)


# reverse_an_array(array_list,left,right)
# print(array_list)

#! check if the given string is palindrome or not

# strin = input("Enter the string you want to check for\n")
# remove_space = strin.lower().replace(" ","")
# num = len(remove_space)


# def check_for_palindrome(i,string,num):
#   if i > int(num/2):
#     return True
#   else:
#     if string[i] != string[num - i -1]:
#       return False
#     else:
#       return check_for_palindrome(i+1,string,num)
    
# ans = check_for_palindrome(0,remove_space,num)
# print(ans)

#! fibonacci number
#? basic approch

# def fibo(num):
#   if num == 0:
#     return 0
#   elif num == 1:
#     return 1
#   else:
#     return fibo(num-1)+fibo(num-2)
  
# print(fibo(6))

# def fib(num):
#   if num <= 0:
#     return num 
#   else:
#    return fib(num - 1)+ fib(num - 2)
  
# print(fib(6))

#! print the subsquence of the array

# arr = []

# size_of_arr =  int(input("Enter the size of the array\n"))
# for i in range(0,size_of_arr):
#   elem = int(input(f"Enter the element at the {i}th position\n"))
#   arr.append(elem)

# # print(arr)
# emp_lis = []

# def print_subsec(index,arr,lis,n):
#   if index == n:
#     print(lis)
#     return
#   else:
#     lis.append(arr[index])
#     print_subsec(index+1,arr,lis,n)
#     lis.pop()
#     print_subsec(index+1,arr,lis,n)

# print_subsec(0,arr,emp_lis,size_of_arr)


#! finding the subseq containing the sum 

arr = []

size_of_arr =  int(input("Enter the size of the array\n"))
for i in range(0,size_of_arr):
  elem = int(input(f"Enter the element at the {i}th position\n"))
  arr.append(elem)

# print(arr)
# emp_lis = []

#! print all the subsec matching the sum
# def subsec_sum(index,arr,lis,s,target_sum,n):
#   if index == n:
#     if s == target_sum:
#       print(lis)
#     return
#   else:
#     #?taking the element 
#     lis.append(arr[index])
#     s += arr[index]
#     subsec_sum(index+1,arr,lis,s,target_sum,n)
#     s -= arr[index]
#     lis.pop()

#     #?for not taking the elemnt
#     subsec_sum(index+1,arr,lis,s,target_sum,n)

#! only print one subsec matching the sum

# def subsec_sum(index:int,arr:list,lis:list,s:int,target_sum:int,n:int) -> bool:
#   if index == n:
#     if s == target_sum:
#       print(lis)
#       return True
#     return False
#   else:
# #?taking the element 
#     lis.append(arr[index])
#     s += arr[index]
#     if (subsec_sum(index+1,arr,lis,s,target_sum,n) == True):
#         return True
#     s -= arr[index]
#     lis.pop()

#     #?for not taking the elemnt
#     if(subsec_sum(index+1,arr,lis,s,target_sum,n)== True):
#       return True
#     return False

#! count the number of subsec that has the similar sum

def count_subsec(index, arr, target_sum, s,n) -> int:
  if index == n:
    if s == target_sum:
      return 1
    else:
      return 0
  
  s += arr[index]
  left = count_subsec(index+1,arr,target_sum,s,n)

  s -+ arr[index]
  right = count_subsec(index+1,arr,target_sum,s,n)

  return left + right

print(count_subsec(0,arr,2,0,size_of_arr))
  
  
