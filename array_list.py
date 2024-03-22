
#!Largest elemet in the array/list

# list = [12,3,45,3,12,34,33,98]

# largest = list[0]
# for i in range(1,len(list)-1):
#   if list[i] > largest:
#     largest = list[i]

# print(largest)

#! second largest element

# array_list = [2,5,9,6,5,5,8]
# largest = array_list[0]
# second_largest = -1

# for number in range(0,len(array_list)):
#   if array_list[number] > largest:
#     second_largest = largest
#     largest = array_list[number]

#   elif (array_list[number]<largest and array_list[number]>second_largest):
#     second_largest = array_list[number]



# print(largest)
# print(second_largest)

#! second smallest
# import sys

# arr = [5,10,23,9,8,5,6,18,12]

# smallest = arr[0]
# s_smallest = sys.maxsize

# for number in range(1, len(arr)):
#   if arr[number] < smallest:
#     s_smallest = smallest
#     smallest = arr[number]

#   elif arr[number]!= smallest and arr[number]< s_smallest:
#     s_smallest = arr[number]

# print(s_smallest)

#! is array sorted (non decending order)

# arr = [4,5,4,4,4,4]

# def check_sorted(arr):
#   for num in range(1, len(arr)):
#     if arr[num] < arr[num - 1]:
#       return False
  
#   return True
    
# print(check_sorted(arr))

#! remove duplicate and return the number of unique elem

# arr = [1,1,2,2,3,4,6,6,7]

# num_set = set()

# for num in arr:
#   num_set.add(num)

# print(len(num_set))

#? optimal two pointer approach
# def unique_element_size_arr(arr,n):
#   i = 0
#   for j in range(1,n):
#     if arr[j] != arr[i]:
#       arr[i+1] = arr[j]
#       i += 1
#   return i+1

# print(unique_element_size_arr(arr,len(arr)))

#! left rotate the array by one 

# arr = [10,20,3,2,4,5,1,4,23,46,76]

# n = len(arr)

# temp = [0] * n
# for i in range(1,n):
#   temp[i-1] = arr[i]
# temp[n-1] = arr[0]

# print(temp)

# temp = arr[0]
# for i in range(0,n-1):
#   arr[i] = arr[i+1]
# arr[n-1] = temp

# print(arr)

#! rotate left by d places

# def left_rotate_by_d(arr,n,d):
#   d = d%n 
#   temp = []
#   for i in range(0,d):
#     temp.append(arr[i])

#   for j in range(d,n):
#     arr[j-d] = arr[j]

#   for i in range(n-d,n):
#     arr[i] = temp[i-(n-d)]

#   return arr
  


# array = [10,23,3,4,5,6,1,3]
# n = len(array)

# left_rotated = left_rotate_by_d(array,n,10)
# print(left_rotated)

#? Optimal 

# arr = [10,2,3,4,56,6]
# arr.reverse()
# print(arr)

# def reverse(arr,str,end):
#   while str<end:
#     arr[str],arr[end] = arr[end],arr[str]
#     str += 1
#     end -= 1

# def rotate_by_d(arr,n,d):
#   d = d%n

#   reverse(arr,0,d-1)
#   reverse(arr,d,n-1)
#   reverse(arr,0,n-1)


# arr = [10,23,45,66,23,56,45,62]
# n = len(arr)
# rotate_by_d(arr,n,2)
# print(arr)
#! ecluidian algo

# def cal_gcd(a,b):
#   if a == 0:
#     return b
#   return cal_gcd(b%a,a)

# a =int(input("Enter a number"))
# b =int(input("Enter another number"))
# print(f"The GCD is of {a} and {b} is {cal_gcd(a,b)}")

#! move zeroes to the end
#? brute

# arr = [1,2,0,7,0,5,3,0,7,4,0,66,0,4,0,0,5]

# temp = []

# for i in range(0,len(arr)):
#   if arr[i] != 0:
#     temp.append(arr[i])

# non_zero_value = len(temp)

# for i in range(0,non_zero_value):
#   arr[i] = temp[i]

# for i in range(non_zero_value,len(arr)):
#   arr[i] = 0

# print(arr)

#? optimal

# j = -1
# for i in range(0,len(arr)):
#   if arr[i] == 0:
#     j = i
#     break

# for i in range(j+1,len(arr)):
#   if arr[i] != 0:
#     arr[i],arr[j] = arr[j],arr[i]
#     j += 1

# print(arr)

#! union in two sorted array 

#? Brute force

# arr1 = [1,1,2,4,5,6,3,4]
# arr2 = [3,4,5,7,8,9,9,1,4]

# uni = set()

# for i in range(0,len(arr1)):
#   uni.add(arr1[i])

# for i in range(0,len(arr2)):
#   uni.add(arr2[i])

# union_arr = [num for num in uni]

#? Optimal

# def union_array(arr1,arr2):
#   n1 = len(arr1)
#   n2 = len(arr2)
#   i = 0
#   j = 0

#   union_arr = []

#   while(i< n1 and j<n2):
#     if(arr1[i] <= arr2[j]):
#       if(len(union_arr) == 0 or union_arr[-1]!=arr1[i]):
#         union_arr.append(arr1[i])
#       i+= 1

#     else:
#       if(len(union_arr) == 0 or union_arr[-1]!= arr2[j]):
#         union_arr.append(arr2[j])
#       j+=1

#   while(j<n2):
#     if(len(union_arr) == 0 or union_arr[-1]!= arr2[j]):
#       union_arr.append(arr2[j])
#     j+=1

#   while(i<n1):
#     if(len(union_arr) == 0 or union_arr[-1]!=arr1[i]):
#       union_arr.append(arr1[i])
#     i+= 1
  
#   return union_arr

# arr1 = [1,1,2,4,5,6]
# arr2 = [3,4,5,7,8,9,9]
# print(union_array(arr1,arr2))
# print(union_array)


#! intersection of two sorted arrays

#? brute
arr1 = [1,1,2,3,4,5,6]
arr2 = [1,2,3,3,4,4,6,7]

n1 = len(arr1)
n2 = len(arr2)

# visted_array = [0]*len(arr2)

# intersection_array = []

# for i in range(0,n1):
#   for j in range(0,n2):
#     if(arr1[i] == arr2[j] and visted_array[j]==0):
#       intersection_array.append(arr1[i])
#       visted_array[j] = 1
#       break

#     if(arr2[j]>arr1[i]):
#       break

# print(intersection_array)

#? optimal
 
# i = 0 
# j = 0
# answer = []

# while(i<n1 and j<n2):
#   if (arr1[i] < arr2[j]):
#     i += 1

#   elif(arr1[i] > arr2[j]):
#     j+= 1

#   elif(arr1[i] == arr2[j]):
#     answer.append(arr1[i])
#     i+=1
#     j+=1


# print(answer)

#! missing number in an arry 

#? brute force

# arr = [1,2,3,4]
# n = 5

# for i in range(1,n+1):
#   flag = 0
#   for j in range(0,n-1):
#     if arr[j] == i:
#       flag = 1
#       break

#   if flag == 0:
#     print(i)

#? better
# hased_array = [0] * int(n+1)
# # print(hased_array)
# for i in range(0,n-1):
#   hased_array[arr[i]] = 1

# # print(hased_array)
# for i in range(1,n+1):
#   if hased_array[i] == 0:
#     print(i)

#?Optimal 

#! using sum
# def missing_elemet(arr,n):
#   sum_0f_n = n*(n+1)//2
#   s1 = 0
#   for i in range(0,n-1):
#     s1 += arr[i]

#   difference = sum_0f_n - s1
#   return difference

# print(missing_elemet(arr,n))

# #! using xor

# def missing_num(arr,n):
#   xor1 = 0
#   for i in range(1,n+1):
#     xor1 = xor1 ^ i
  
#   xor2 = 0
#   for i in range(0,n-1):
#     xor2 = xor2 ^ arr[i]



#   return xor1 ^ xor2

# print(missing_num(arr,n))

#! max consicutive ones

# def finding_max_consi_ones(arr,n,num):
#   maximum = 0
#   count = 0

#   for i in range(0,n):
#     if arr[i] == num:
#       count += 1
#       maximum = max(maximum,count)
#     else:
#       count = 0
  
#   return maximum

# arr = [0,0,1,1,1,0,1,1,1,1,1,0,0,1]
# n = len(arr)

# print(finding_max_consi_ones(arr,n,1))

#! element with the single occurance in the list

# def single_occure(arr,n):
#   xor = 0
#   for i in range(n):
#     xor = xor ^ arr[i]
  
#   return xor

# arr = [1,1,2,2,3,4,4]
# n = len(arr)

# print(single_occure(arr,n))

#! find max len of the subarray having sum is K

# def find_max_subarray(arr,k):
#   n = len(arr)
#   summ = 0
#   max_l = 0
#   pre_sum_map = {}

#   for i in range(n):
#     summ += arr[i]

#     if summ == k:
#       max_l = max(max_l,(i+1))

#     rem = summ - k

#     if rem in pre_sum_map:
#       length =  i - pre_sum_map[rem]
#       max_l = max(max_l,length)

#     if summ not in pre_sum_map:
#       pre_sum_map[summ] = i
  
#   return max_l


# arr = [2,3,5,1,9]
# k = 10

# print(find_max_subarray(arr,k))

#! Optimal 

def find_max_subarray_sum(arr,k):
  n = len(arr)
  rgt = 0
  lft = 0
  total = arr[0]
  max_l = 0

  while(rgt < n):
    while(lft <= rgt and total > k):
      total -= arr[lft]
      lft += 1

    if total == k:
      max_l = max(max_l, rgt - lft + 1)

    rgt += 1
    if (rgt < n ):
      total += arr[rgt]
  
  return max_l


arr = [2,3,5,1,9]
k = 8

print(find_max_subarray_sum(arr,k))