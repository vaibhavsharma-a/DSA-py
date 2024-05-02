
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


# #! deffi helman
# # Diffie-Hellman Code


# def prime_checker(p):
# 	# Checks If the number entered is a Prime Number or not
# 	if p < 1:
# 		return -1
# 	elif p > 1:
# 		if p == 2:
# 			return 1
# 		for i in range(2, p):
# 			if p % i == 0:
# 				return -1
# 			return 1


# def primitive_check(g, p, L):
# 	# Checks If The Entered Number Is A Primitive Root Or Not
# 	for i in range(1, p):
# 		L.append(pow(g, i) % p)
# 	for i in range(1, p):
# 		if L.count(i) > 1:
# 			L.clear()
# 			return -1
# 		return 1


# l = []
# while 1:
# 	P = int(input("Enter P : "))
# 	if prime_checker(P) == -1:
# 		print("Number Is Not Prime, Please Enter Again!")
# 		continue
# 	break

# while 1:
# 	G = int(input(f"Enter The Primitive Root Of {P} : "))
# 	if primitive_check(G, P, l) == -1:
# 		print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
# 		continue
# 	break

# # Private Keys
# x1, x2 = int(input("Enter The Private Key Of User 1 : ")), int(
# 	input("Enter The Private Key Of User 2 : "))
# while 1:
# 	if x1 >= P or x2 >= P:
# 		print(f"Private Key Of Both The Users Should Be Less Than {P}!")
# 		continue
# 	break

# # Calculate Public Keys
# y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# # Generate Secret Keys
# k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

# print(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")

# if k1 == k2:
# 	print("Keys Have Been Exchanged Successfully")
# else:
# 	print("Keys Have Not Been Exchanged Successfully")

# #! set matrix zero

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

#? Optimal

# def optimal_set_matrix_0(matrix,n,m):
#   col0 = 1
#   for i in range(n):
#     for j in range(m):
#       if matrix[i][j] == 0:
#         matrix[i][0] = 0

#         if j != 0:
#           matrix[0][j] = 0
#         else:
#           col0 = 0

#   for i in range(1,n):
#     for j in range(1,m):
#       if matrix[i][j] != 0:
#         if matrix[i][0] == 0 or matrix[0][j] == 0:
#           matrix[i][j] = 0

#   if matrix[0][0] == 0:
#     for j in range(m):
#       matrix[0][j] = 0

#   if col0 == 0:
#     for i in range(n):
#       matrix[i][0] = 0

#   return matrix


# matrix = [[1,1,0,1],[0,1,1,1],[1,1,1,0],[1,1,1,1]]
# n = len(matrix)
# m = len(matrix[0])
# for i in range(n):
#   for j in range(m):
#     print(matrix[i][j], end=" ")
#   print()
# print("--------------------------------------")
# ans = optimal_set_matrix_0(matrix,n,m)
# for i in range(n):
#   for j in range(m):
#     print(ans[i][j], end=" ")
#   print()


#! rotate by 90 clockwise

#? brute
# import numpy as np
# def rotate_mat(matrix,n):
#   rotated = [[0 for _ in range(n)]for _ in range(n)]
#   # rotated = np.zeros([n,n],dtype=int) #? can use numpy to create arrays
#   print(rotated)
#   for i in range(n):
#     for j in range(n):
#       rotated[j][n-1-i] = matrix[i][j]
#   return rotated

# matrix = [[2,3,4,5],[4,5,6,2],[3,4,7,8],[6,7,1,0]]
# n = len(matrix)
# # m = len(matrix[0])
# for i in range(n):
#   for j in range(n):
#     print(matrix[i][j], end=" ")
#   print()
# print("--------------------------------------")
# ans = rotate_mat(matrix,n)
# for i in range(n):
#   for j in range(n):
#     print(ans[i][j], end=" ")
#   print()

#? optimal

# def transpose(matrix,n):
#   for i in range(n-1):
#     for j in range(i+1,n):
#         matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
#   # return matrix

# def reverse_row(matrix):
#   for rows in matrix:
#     rows.reverse()

# def rotate_by_90(matrix,n):
#   transpose(matrix,n)
#   reverse_row(matrix)
#   return matrix

# matrix = [[2,3,4,5],[4,5,6,2],[3,4,7,8],[6,7,1,0]]
# n = len(matrix)
# # m = len(matrix[0])
# for i in range(n):
#   for j in range(n):
#     print(matrix[i][j], end=" ")
#   print()
# print("--------------------------------------")
# ans = rotate_by_90(matrix,n)
# for i in range(n):
#   for j in range(n):
#     print(ans[i][j], end=" ")
#   print()


#! print in spiral

#? optimal

# def print_spiral(matrix):
#   n = len(matrix)
#   m = len(matrix[0])

#   top = 0
#   bot = n - 1
#   lft = 0
#   rgt = m - 1
#   ans = []

#   while(lft <= rgt and top <= bot):
#     for i in range(lft,rgt+1):
#       ans.append(matrix[top][i])

#     top += 1

#     for i in range(top,bot+1):
#       ans.append(matrix[i][rgt])
#     rgt -= 1

#     if top <= bot:
#       for i in range(rgt,lft-1,-1):
#         ans.append(matrix[bot][i])
#       bot -= 1
    
#     if lft <= rgt:
#       for i in range(bot,top-1,-1):
#         ans.append(matrix[i][lft])
#       lft += 1
#   return ans

# matrix = [[2,3,4,5],
#           [4,5,6,2],
#           [3,4,7,8],
#           [6,7,1,0]]
# n = len(matrix)
# m = len(matrix[0])
# for i in range(n):
#   for j in range(n):
#     print(matrix[i][j], end=" ")
#   print()
# print("--------------------------------------")
# ans = print_spiral(matrix)
# print(ans)

#! count the number of subarray with presum k

#? optimal

# def count_subarray_sum(arr,k):
#   presum = 0
#   premap ={}
#   cnt = 0
#   premap[0] = 1
#   for num in arr:
#     presum += num
#     rem = presum - k
#     if rem in premap:
#       cnt += premap[rem]
#     if presum not in premap:
#       premap[presum] = 1
#     else:
#       premap[presum] += 1
#   return cnt

# arr = [1,2,3,-3,1,1,1,4,2,-3]
# k = 3
# print(count_subarray_sum(arr,k))

#! Pascal triangle

#! Type 1 problem :
#? Given R and C find the elemet present there

# def nCr(n,r):
#   res = 1
#   for i in range(r):
#     res = res*(n-i)
#     res = res//(i+1)
#   return res

# def find_elm_at_r_c(r,c):
#   return nCr(r-1,c-1)

# print(find_elm_at_r_c(5,3))

#! type 2 problem
#? print the nth row of the pascal triangle
#? brute

# def print_Row(n):
#   for c in range(1,n+1):
#     print(nCr(n-1,c-1),end=" ")


# print_Row(4)

#? Optimal

# def print_row(n):
#   ans_list = []
#   ans =  1
#   ans_list.append(ans)
#   for i in range(1,n):
#     ans = ans*(n-i)
#     ans = ans//i
#     ans_list.append(ans)
#   return ans_list

# print(print_row(3))


#! type 3
# #? generate the pascal tringle upto n row

# def generate_row(row):
#   ans = 1
#   ans_list = []
#   ans_list.append(1)
#   for col in range(1,row):
#     ans = ans * (row - col)
#     ans = ans//col
#     ans_list.append(ans)
#   return ans_list

# def generate_triangle(n):
#   trianlge = []
#   for i in range(1,n+1):
#     trianlge.append(generate_row(i))

#   return trianlge

# print(generate_triangle(5))

#! marjority element more than n/3 times

# def majority_n3(arr,n):
#   list = []
#   for i in range(n):
#     if len(list) == 0 or list[0]!= arr[i]:
#       cnt = 0
#       for j in range(n):
#         if arr[j] == arr[i]:
#           cnt+=1
#       if cnt > n//3:
#         list.append(arr[i])
    
#     if len(list) == 2:
#       break
#   return list

# arr = [1,1,1,2,2,3,3,3]
# n = len(arr)
# print(majority_n3(arr,n))


#? better solution

# from collections import defaultdict

# def major_n3_better(arr,n):
#   mini = (n//3) + 1
#   map = defaultdict(int)
#   list = []
#   for num in arr:
#     map[num]+= 1
#     if map[num] == mini:
#       list.append(num)
#   return list


# arr = [1,1,1,1,2,3,3,3]
# n = len(arr)
# print(major_n3_better(arr,n))


# #? optimal

# def majorityElement(v):
#     el1 = -float('inf')
#     el2 = -float('inf')
#     cnt1 = 0
#     cnt2 = 0
#     n = len(v)
#     for num in v:
#         if cnt1 == 0 and el2 != num:
#             cnt1 = 1
#             el1 = num
#         elif cnt2 == 0 and el1!= num:
#             cnt2 =1
#             el2 = num
#         elif el1 == num:
#             cnt1 += 1
#         elif el2 == num:
#             cnt2 += 1
#         else:
#             cnt1 -= 1
#             cnt2 -= 1
#     cnt1 = 0
#     cnt2 = 0
#     lis = []
#     mini = (n//3) + 1
#     for num in v:
#         if num ==  el1:
#             cnt1+=1
#         if num == el2:
#             cnt2 += 1
#     if cnt1 >= mini:
#         lis.append(el1)
#     if cnt2 >= mini:
#         lis.append(el2)
#     lis.sort()
#     return lis

# def overlapping(arr):
#     # lis = [[1,3],[8,10],[2,6],[15,18]]
#     arr.sort()
#     ans = []
#     n = len(arr) # this wll be the size of the main list that contain other small lists

#     for i in range(n):
#         strt = arr[i][0]
#         end = arr[i][1]
#         if ans and end <= ans[-1][1]:
#             continue

#!combine two sorted array into one no extra space for optimal

#? brute

# def combine(arr1,arr2,n,m):
#   arr3 = [0]*int(m+n)
#   left = 0
#   right = 0
#   index = 0
#   while left < n and right < m:
#     if arr1[left] <= arr2[right]:
#         arr3[index] = arr1[left]
#         index += 1
#         left += 1
#     else:
#         arr3[index] = arr2[right]
#         index += 1
#         right += 1
#   while left < n:
#      arr3[index] = arr1[left]
#      index += 1
#      left += 1
#   while right<m:
#      arr3[index] = arr2[right]  
#      index += 1
#      right += 1

#   for i in range(n+m):
#     if i < n:
#         arr1[i] = arr3[i]
#     else:
#        arr2[i - n] = arr3[i]
#   return arr1,arr2


# arr1 = [1,4,8,9]
# arr2 = [2,3,5,7]
# n = len(arr1)
# m = len(arr2)
# print(combine(arr1,arr2,n,m))


# #? optimal 

# def combinesorted(arr1,arr2):
#   n = len(arr1)
#   m = len(arr2)
#   left  = n-1
#   right = 0
#   while left >= 0 and right < m:
#     if arr1[left] > arr2[right]:
#       arr1[left],arr2[right] = arr2[right],arr1[left]
#       left -= 1
#       right += 1
#     else:
#       break
#   arr1.sort()
#   arr2.sort()
#   return arr1,arr2

# arr1 = [1,4,8,9]
# arr2 = [2,3,5,7]
# print(combinesorted(arr1,arr2))


#! find missing and repeated array

#?better solution

# def missing_reapearting(arr,n):
#   hashed_arr = [0]*int(n+1)
#   for i in range(n):
#     hashed_arr[arr[i]] += 1
#   # print(hashed_arr)
#   missing = -1 
#   repeating = -1
#   for i in range(1,n+1):
#     if hashed_arr[i] == 2:
#       repeating = i
#     elif hashed_arr[i] == 0:
#       missing = i
    
#     if repeating != -1 and missing != -1:
#       break
#   return [missing,repeating]

# arr = [2,4,3,6,1,1]
# n = len(arr)

# print(missing_reapearting(arr,n))


# def floorSqrt(n):
#    # write your code logic here .
#     low = 1
#     high = n
#     # Binary search on the answers:
#     while low <= high:
#         mid = (low + high) // 2
#         val = mid * mid
#         if val <= n:
#             # Eliminate the left half:
#             low = mid + 1
#         else:
#             # Eliminate the right half:
#             high = mid - 1
#     return high


# print(floorSqrt(7))



# def getmax(arr,n):
#     maxi = arr[0]
#     for i in range(n):
#         if arr[i] > maxi:
#             maxi = arr[i]
#     return maxi


# arr = [2,3,11,6]
# n = len(arr)

# print(getmax(arr,n))

# import math

# ans = math.ceil(11//2)
# ans2 = math.ceil(11/2)

# print(ans)
# print(ans2)



import matplotlib.pyplot as plt
# import numpy as np

# # Number of users
# num_users = 100

# # Generate x-axis values representing users (10, 20, 30, ..., 100)
# users = np.arange(10, num_users + 1, 10)

# # Generate sample data for acceptance rate
# # For simplicity, let's generate a linearly increasing acceptance rate
# base_acceptance_rate = np.linspace(0.5, 0.9, len(users))  # Linearly increasing acceptance rate
# acceptance_rate = base_acceptance_rate + np.random.normal(0, 0.02, len(users))  # Adding noise for small dips

# # Plotting the acceptance rate in blue
# plt.plot(users, acceptance_rate, color='green', label='Acceptance Rate')

# # Adding labels to the axes and a title
# plt.xlabel('Number of Users')
# plt.ylabel('Acceptance Rate')
# plt.title('Acceptance Rate')

# # Adding a legend
# plt.legend()

# # Displaying the plot
# plt.grid(True)
# plt.show()


# no_of_tries =[20,40,60,80,100]

# far = [0,0,0,1,3]
# frr = [1,2,3,5,6]



# plt.plot(no_of_tries,far,color="Green",label = "FAR",linewidth = "3.3",linestyle ="-")
# plt.plot(no_of_tries,frr,color="red",label = "FRR",linewidth = "3.3",linestyle ="-")

# plt.xlabel("Number of tries",fontsize = 14, fontstyle = "italic")
# plt.ylabel("Error in tries FAR/FRR",fontsize = 14, fontstyle = "italic")


# plt.legend(fontsize=12, shadow=True, frameon=True)

# for i in range(len(no_of_tries)):
#     plt.hlines(y=far[i], xmin=0, xmax=no_of_tries[i], color='gray', linestyle='dashed', linewidth=1, alpha=0.5)
#     plt.hlines(y=frr[i], xmin=0, xmax=no_of_tries[i], color='gray', linestyle='dashed', linewidth=1, alpha=0.5)

# # Display only horizontal gridlines
# plt.grid(axis='y')

# plt.scatter(no_of_tries, far, color='green', marker='o', edgecolor='Green')
# plt.scatter(no_of_tries, frr, color='red', marker='o', edgecolor='red')

# plt.ylim(-1, 8)
# plt.yticks(range(9))

# plt.show()

def print_char_frequency(s):
    # Count the frequency of each character
    char_frequency = {}
    for char in s:
        # char_frequency[char] = char_frequency.get(char, 0) + 1
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1

    # print(char_frequency)
    
    # Sort the characters based on their ASCII values
    sorted_chars = sorted(char_frequency.keys())
    # print(sorted_chars)

    # Print the characters and their frequencies
    for char in sorted_chars:
        print(f"{char} --> {char_frequency[char]}")

# Example usage
s = "azaaaBccdAeeb"
print_char_frequency(s)



