
#! 2 sum
#? brute

# def Twosum_brute(arr,tar):
#   n = len(arr)
#   for i in range(n):
#     for j in range(i+1,n):
#       if i == j:
#         continue

#       if arr[i] + arr[j] == tar:
#         print("Yes")
#         return i,j
      
# arr = [1,3,4,7,9]
# k = 5
# print(Twosum_brute(arr,k))

#? better

# def twosum_better(arr,k):
#   check = {}
#   n = len(arr)
#   for i in range(n):
#     a = arr[i]
#     rest = k - a

#     if rest in check:
#       print("Yes")
#       return check[rest],i 

#     if a not in check:
#       check[a] = i

#   return "No"


# arr = [1,1,3,4,7,9]
# k = 5
# print(twosum_better(arr,k))

#? bit better than better if we need to only give result i true or false

# def twosum_twopointer(arr,k):
#   n = len(arr)
#   lft = 0
#   rgt = n-1
#   arr.sort()
#   while(lft<rgt):
#     total = arr[lft] + arr[rgt]
#     if total == k:
#       return True
#     elif k > total:
#       lft += 1
#     else:
#       rgt -= 1
  
#   return False

# arr = [2,1,9,8,5,3]
# k = 10

# print(twosum_twopointer(arr,k))

#! sort the array containing only 0,1 and 2

# def sort_0_1_2(arr,n):
#   ct0 = 0
#   ct1 = 0
#   ct2 = 0

#   for i in range(n):
#     if arr[i] == 0:
#       ct0 += 1
#     elif arr[i] == 1:
#       ct1 += 1
#     else:
#       ct2 += 1

#   for i in range(0,ct0):
#     arr[i] = 0
#   for i in range(ct0,(n - ct1) + 1):
#     arr[i] = 1
#   for i in range((n - ct1) + 1,n):
#     arr[i] = 2


# arr = [0,1,2,2,2,0,0,1,0,1,0,0,1]
# n = len(arr)
# sort_0_1_2(arr,n)
# print(arr)

# def swap(arr,lft,rgt):
#   arr[lft],arr[rgt] = arr[rgt],arr[lft]

# def sort_0_1_2(arr,n):
#   low = 0
#   mid = 0
#   hgh = n - 1
#   while(mid <= hgh):
#     if arr[mid] == 0:
#       swap(arr,low,mid)
#       low += 1
#       mid += 1
#     elif arr[mid] == 1:
#       mid += 1
#     else:
#       swap(arr,mid,hgh)
#       hgh -= 1

# arr = [1,2,0,0,0,1,1,2,2,0,0,1,0]
# n = len(arr)
# sort_0_1_2(arr,n)
# print(arr)

#! majority element > n/2 times

# def majority_elm(arr,n):
#   for i in range(n):
#     cnt = 0
#     for j in range(n):
#       if arr[j] == arr[i]:
#         cnt += 1

#     if cnt > int(n/2):
#       return arr[i]
    
#   return -1

# arr = [2,2,1,3,1,2,2,2]
# n = len(arr)
# print(majority_elm(arr,n))

#? better

# def better_majority(a):
#   n =len(a)
#   count = {}
#   for i in a:
#     if i in count:
#       count[i] += 1
#     else:
#       count[i] = 1

#   for elem,occr in count.items():
#     if occr > n//2:
#       return elem
#   return -1

# arr = [2,2,2,3,1,1,2,2]
# print(better_majority(arr))

#? Optimal Moore's voting algo

# def optimal_majority(arr,n):
#   cnt = 0
#   elm = None
#   for i in range(n):
#     if cnt == 0:
#       cnt = 1
#       elm = arr[i]
#     elif elm == arr[i]:
#       cnt += 1
#     else:
#       cnt -= 1

#   cnt1 = 0
#   for i in range(n):
#     if arr[i] == elm:
#       cnt1 += 1
  
#   if cnt1 > n//2:
#     return elm
  
#   return -1

#! to find the max sum of sub array

#? brute

# def max_sum_subarray(arr):
#   n = len(arr)
#   maxi = 0
#   for i in range(n):
#     for j in range(i,n):
#       sum = 0
#       for k in range(i,j):
#         sum += arr[k]
#         maxi = max(maxi,sum)
#   return maxi

# arr = [-2,-3,4,-1,-2,1,5,-3]
# print(max_sum_subarray(arr))

#? better 

# def max_sub_sum(arr,n):
  # maxi = -float('inf')
#   for i in range(n):
#     sum = 0
#     for j in range(i,n):
#       sum += arr[j]
#       maxi = max(maxi,sum)

#   return maxi

# arr = [-2,-3,4,-1,-2,1,5,-3]
# n = len(arr)
# print(max_sub_sum(arr,n))

#? optimal 
#! kadan's algorith

# def kdan_sub_sum(arr):
#   sum = 0
#   maxi = -float('inf')
#   for num in arr:
#     sum += num
#     maxi = max(maxi,sum)
#     if sum < 0:
#       sum = 0
#   return maxi

# arr = [-2,-3,4,-1,-2,1,5,-3]
# print(kdan_sub_sum(arr))

#! buy and sell stock at max profit

# def buy_sell_stock(arr,n):
#   mini = arr[0]
#   profit = 0
#   for i in range(n):
#     cost = arr[i] - mini #?this will tell the amount of profit or loss that we have got by selling stock on i^th day
#     profit = max(profit,cost) #?this will give the max profit out of the previous max and current cost 
#     mini = min(mini,arr[i]) #?this will update the mini value to the minimum from 0 to i-1
#   return profit

# stocks = [7,1,2,4,5,3,2]
# n = len(stocks)
# print(buy_sell_stock(stocks,n)) #?we buy at 1 and sell at 5 to get max profit of 4

#! rearrange array by sign

#? brute

# def reaaraage_by_sign(arr,n):
#   pos_arr = []
#   neg_arr = []
#   for i in range(n):
#     if arr[i]<0:
#       neg_arr.append(arr[i])
#     else:
#       pos_arr.append(arr[i])
#   # print(pos_arr)
#   # print(neg_arr)

#   for i in range(n//2):
#     arr[2*i] = pos_arr[i]
#     arr[(2*i)+1] = neg_arr[i]
  
#   return arr

# arr = [-2,3,-1,2,6,-9]
# n = len(arr)
# print(reaaraage_by_sign(arr,n))

#? optimized
# def arrange_bysign(arr,n):
#   pos_index = 0
#   neg_index = 1
#   arr_arrange = [0]*n
#   for i in range(n):
#     if arr[i] < 0:
#       arr_arrange[neg_index] = arr[i]
#       neg_index += 2
#     else:
#       arr_arrange[pos_index] = arr[i]
#       pos_index += 2
#   return arr_arrange

# arr = [-2,3,-1,2,6,-9]
# n = len(arr)
# print(arrange_bysign(arr,n))

#! generate permutations

# from typing import List

# def recur_permutation(data_Struc: List[int], nums: List[int], ans : List[List[int]], freq : List[int] ):
#   if len(data_Struc) == len(nums):
#     ans.append(data_Struc[:])
#     return
#   for i in range(len(nums)):
#     if freq[i] == 0:
#       data_Struc.append(nums[i])
#       freq[i] = 1
#       recur_permutation(data_Struc,nums,ans,freq)
#       freq[i] = 0
#       data_Struc.pop()

# def permutation(nums : List[int]):
#   data_struct = []
#   ans = []
#   freq = [0]*len(nums)
#   recur_permutation(data_struct,nums,ans,freq)
#   return ans

# nums = [1,2,3]
# print(permutation(nums))

#! next permutation of an array

#? optimal

# def reverse(arr,str,end):
#   while str<end:
#     arr[str],arr[end] = arr[end],arr[str]
#     str += 1
#     end -= 1

# def nxt_permu(arr,n):
#   ind = -1
#   for i in range(n-2,-1,-1):
#     if arr[i] < arr[i+1]:
#       ind = i
#       break
#   if ind == -1:
#     reverse(arr,0,n-1)
#     return arr
  
#   for i in range(n-1,ind,-1):
#     if arr[i] > arr[ind]:
#       arr[i],arr[ind] = arr[ind],arr[i]
#       break
  
#   reverse(arr,ind+1,n-1)

#   return arr


# arr = [3,2,1]
# n=len(arr)
# print(nxt_permu(arr,n))

#! leader in an array

#? brute force
# def leader_arr(arr,n):
#   ans = []
#   for i in range(n):
#     leader = True
#     for j in range(i+1,n):
#       if arr[j] > arr[i]:
#         leader = False
#         break
  
#     if leader == True:
#       ans.append(arr[i])
  
#   return ans

# arr = [2,5,19,15,10,12,3]
# n = len(arr)
# print(leader_arr(arr,n))

#? Optimal

# def superior_element(arr,n):
#   maxi = -float('inf')
#   ans = []
#   for i in range(n-1,-1,-1):
#     if arr[i] > maxi:
#       ans.append(arr[i])
    
#     maxi = max(maxi,arr[i])

#   return ans

# arr = [2,5,19,15,10,12,3]
# n = len(arr)
# print(superior_element(arr,n))

#! longest consecutive subarray 

#? brute

# def linear_search(a,num):
#   for i in a:
#     if i == num:
#       return True
#   return False


# def longest_consecutive_array(a,n):
#   longest = 1
#   for i in range(n):
#     x = a[i]
#     cnt = 1
#     while(linear_search(a,x+1) == True):
#       x = x+1
#       cnt += 1
    
#     longest = max(longest,cnt)
#   return longest


# a = [1,103,2,101,4,3,102]
# n = len(a)
# print(longest_consecutive_array(a,n))

#? better 

# def better_consec_sub(arr,n):
#   arr.sort()
#   longest = 1
#   last_small = -float('inf')
#   cnt = 0
#   for i in range(n):
#     if arr[i] - 1 == last_small:
#       cnt += 1
#       last_small = arr[i]
#     elif arr[i] != last_small:
#       cnt = 1
#       last_small = arr[i]

#     longest = max(longest,cnt)
#   return longest

# a = [1,103,2,101,4,3,102]
# n = len(a)
# print(better_consec_sub(a,n))


#todo : will preserve the order while iterating over the list to store single element but will not sort them
# from collections import OrderedDict as od
# lis = [1,1,3,3,2,3,4,1,4,6,3,7,8,6,5,8,2]
# som = od.fromkeys(lis)

# print(list(som.keys()))

#? Optimal

# def optimal_consec_sub(arr,n):
#   if n == 0:
#     return 0
  
#   longest = 1
#   num_set =  set()

#   for num in arr:
#     num_set.add(num)

#   for num in num_set:

#     if num - 1 not in num_set:
#       cnt = 1
#       x = num
#       while x+1 in num_set:
#         x += 1
#         cnt += 1

#       longest = max(longest,cnt)
  
#   return longest

# a = [1,103,2,101,4,3,102]
# n = len(a)
# print(optimal_consec_sub(a,n))

#! RSA digital signature services

# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives.asymmetric import rsa

# # Generate RSA key pair
# private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
#     backend=default_backend()
# )
# public_key = private_key.public_key()

# # Message to be signed
# message = b"Hello, world!"

# # Sign the message
# signature = private_key.sign(
#     message,
#     padding.PSS(
#         mgf=padding.MGF1(hashes.SHA256()),
#         salt_length=padding.PSS.MAX_LENGTH
#     ),
#     hashes.SHA256()
# )

# # Verify the signature
# try:
#     public_key.verify(
#         signature,
#         message,
#         padding.PSS(
#             mgf=padding.MGF1(hashes.SHA256()),
#             salt_length=padding.PSS.MAX_LENGTH
#         ),
#         hashes.SHA256()
#     )
#     print("Signature is valid. Message is authentic.")
# except:
#     print("Invalid signature. Message may have been tampered with.")

#! set matrix zero

#? brute

# def set_row(i,matrix,m):
#   for j in range(m):
#     if matrix[i][j] != 0:
#       matrix[i][j] = -1

# def set_col(j,matrix,n):
#   for i in range(n):
#     if matrix[i][j] != 0:
#       matrix[i][j] = -1

# def set_matrix(matrix,n,m):
#   for i in range(n):
#     for j in range(m):
#       if matrix[i][j] == 0:
#         set_row(i,matrix,m)
#         set_col(j,matrix,n)

  
#   for i in range(n):
#     for j in range(m):
#       if matrix[i][j] == -1:
#         matrix[i][j] = 0

#   return matrix

# matrix = [[1,1,0,1],[1,1,1,1],[1,1,1,0]]
# n = len(matrix)
# m = len(matrix[0])
# for i in range(n):
#   for j in range(m):
#     print(matrix[i][j], end=" ")
#   print()
# print("--------------------------------------")
# ans = set_matrix(matrix,n,m)
# for i in range(n):
#   for j in range(m):
#     print(ans[i][j], end=" ")
#   print()

#? better
# def set_zero_better(matrix,n,m):
#   row = [0] * n
#   col =  [0] * m

#   for i in range(n):
#     for j in range(m):
#       if matrix[i][j] == 0:
#         row[i] = 1
#         col[j] = 1

#   for i in range(n):
#     for j in range(m):
#       if row[i] or col[j]:
#         matrix[i][j] = 0

#   return matrix

  

# matrix = [[1,1,0,1],[0,1,1,1],[1,1,1,0],[1,1,1,1]]
# n = len(matrix)
# m = len(matrix[0])
# for i in range(n):
#   for j in range(m):
#     print(matrix[i][j], end=" ")
#   print()
# print("--------------------------------------")
# ans = set_zero_better(matrix,n,m)
# for i in range(n):
#   for j in range(m):
#     print(ans[i][j], end=" ")
#   print()