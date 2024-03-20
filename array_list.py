
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

arr = [1,1,2,2,3,4,6,6,7]

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

def reverse(arr,str,end):
  while str<end:
    arr[str],arr[end] = arr[end],arr[str]
    str += 1
    end -= 1

def rotate_by_d(arr,n,d):
  d = d%n

  reverse(arr,0,d-1)
  reverse(arr,d,n-1)
  reverse(arr,0,n-1)


arr = [10,23,45,66,23,56,45,62]
n = len(arr)
rotate_by_d(arr,n,2)
print(arr)
#! ecluidian algo

# def cal_gcd(a,b):
#   if a == 0:
#     return b
#   return cal_gcd(b%a,a)

# a =int(input("Enter a number"))
# b =int(input("Enter another number"))
# print(f"The GCD is of {a} and {b} is {cal_gcd(a,b)}")

