"""
! this is to extract digit form a given number
"""
# num = 325467
# last_num = num%10
# print(last_num)
# the_scd_last = (int(num/10))%10
# print(the_scd_last)
# the_thrd_last = int(int(num/10)/10)%10
# print(the_thrd_last)
# the_fort_last = int(int(int(num/10)/10)/10)%10
# print(the_fort_last)
# the_fif_last = int(int(int(int(num/10)/10)/10)/10)%10
# print(the_fif_last)

# num = int(input("Enter any number you wish\n"))
# dig_count = 0
# while num>0:
#   last_dig = num%10
#   print(last_dig,end=" ")
#   num = int(num/10)
#   dig_count += 1


# print(f"\nthe number of digits present in the given number is : {dig_count}")
"""
? reversing a number / armstrong number
"""
# num = input("Enter any number you want\n")
# power = len(num)

# number = int(num)
# dup = number

# amst_num = 0
# # rev_num = 0
# while number > 0:
#   last_dig = number%10
#   # rev_num = (rev_num*10) + last_dig
#   amst_num += last_dig**power
#   number = number // 10

  
# if dup == amst_num:
#   print("True")
# else:
#   print("False")

# print(amst_num)

#? Print all the divisor of a number
import math as m

# number = int(input("Enter any number you want\n"))
# sqrt_num = m.sqrt(number)

# div_lis = []
# for i in range(1,int(sqrt_num+1)):
#   if number%i == 0:
#     div_lis.append(i)
#     if int(number/i) != i:
#       div_lis.append(int(number/i))

# div_lis.sort()
# print(div_lis)
    
#? to check for prime number

# number = int(input("Enter a number\n"))

# sqrt_num = m.sqrt(number)
# count = 0
# for i in range(1,int(sqrt_num+1)):
#   if number%i == 0:
#     count += 1
#     if int(number/i)!= i:
#       count += 1

# if count == 2:
#   print("True")
# else:
#   print("False")

#? GCD OR HCF

# def get_gcd(num1:int,num2:int) -> int:
#   while num1>0 and num2>0:
#     if num1>num2:
#       num1 = num1%num2
#     else:
#       num2 = num2%num1

#   if num1 == 0:
#     return num2
#   else: 
#     return num1

# gcd = get_gcd(52,10)
# print(gcd)



