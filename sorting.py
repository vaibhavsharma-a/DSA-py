
#! selection sort O(n^2): will select and element compare it will the others to find smaller one and swap it
# def selection_sort(array:list,number:int) -> list:
#   for i in range(0,number-1):
#     mini = i
#     for j in range(i,number):
#       if array[j] < array[mini]:
#         mini = j

      
#     temp = array[mini]
#     array[mini] = array[i]
#     array[i] = temp

#   return array
    
# arry = [54, 56, 68, 65, 78, 98]
# n = len(arry)
# sorted_arry = selection_sort(arry,n)
# print(sorted_arry)

#! Bubble sort O(n^2)

# def bubble_sort(arr:list,num:int):
#   for i in range(num-1,-1,-1):
#     did_swap = 0
#     for j in range(0,i):
#       if arr[j]>arr[j+1]:
#         temp = arr[j+1]
#         arr[j+1]= arr[j]
#         arr[j] = temp
#         did_swap =  1
    
#     if did_swap == 0:
#       break
#     print("runs\n")
  


# arry = [1,3,6,8,10,14]
# n = len(arry)
# bubble_sort(arry,n)
# print(arry)


#! insertion sort O(n^2)

# def insertion_sort(arr,num):
#   for i in range(0,num):
#     j = i
#     while j > 0  and arr[j - 1] > arr[j]:
#       temp = arr[j - 1]
#       arr[j - 1] = arr[j]
#       arr[j] = temp
#       j -= 1

# arry = [1,3,6,8,10,14]
# n = len(arry)
# insertion_sort(arry,n)
# print(arry)

#! merge sort (N log base 2 N), space (ON)

# def merge(arr,low,high,mid):
#   temp_arr = []
#   left = low
#   right = mid+1

#   while(left <= mid and right <= high):
#     if arr[left]<=arr[right]:
#       temp_arr.append(arr[left])
#       left += 1
#     else:
#       temp_arr.append(arr[right])
#       right += 1

#   while (left<= mid):
#     temp_arr.append(arr[left])
#     left += 1
  
#   while (right<= high):
#     temp_arr.append(arr[right])
#     right += 1

#   for i in range(low,high+1):
#     arr[i] = temp_arr[i - low]

  

# def merge_sort(arr,low,high):
#   if low >= high :
#     return 
#   else: 
#     mid = int((low+high)/2)
#     merge_sort(arr,low,mid)
#     merge_sort(arr,mid+1,high)
#     merge(arr,low,high,mid)

# arry = [10,2,12,3,45,3,34,49,26]

# n = len(arry)

# merge_sort(arry,0,n-1)
# print(arry)

#! Bubble sort using recurrsion 

# def bubble_Rec(arr:list, number:int) -> None:
#   if number == 1:
#     return
    
#   else:
#     did_swap = 0
#     for j in range(0,number - 1):
#       if arr[j]>arr[j+1]:
#         temp = arr[j+1]
#         arr[j+1] = arr[j]
#         arr[j] = temp 
#         did_swap = 1
  

#   if did_swap == 0:
#     return
  
#   bubble_Rec(arr,number-1)


# arry = [13,24,20,9,46,52]
# n = len(arry)
# bubble_Rec(arry,n)
# print(arry)

#! insertion sort with recursion

# def insertion_rec(arr,index,number):
#   if index == number:
#     return
#   else:
#     j = index
#     while(j>0 and arr[j-1] > arr[j]):
#       temp = arr[j-1]
#       arr[j-1] =  arr[j]
#       arr[j] = temp
#       j -= 1

#     insertion_rec(arr,index + 1,number)
  
# arry = [13,24,20,9,46,52]
# n = len(arry)
# insertion_rec(arry,0,n)
# print(arry)

#! Quick sort algo

# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]

# def patri_index(arr,low,high):
#   pivot = arr[low]
#   i = low
#   j = high
#   while i < j:
#     while (arr[i] <= pivot and i <= high - 1):
#       i += 1

#     while (arr[j] > pivot and j >= low+1):
#       j -= 1

#     if i < j:
#       swap(arr,i,j)

#   swap(arr,low,j)
#   return j

# def q_s(arr,low,high):
#   if low<high:
#     pindex = patri_index(arr,low,high)
    
#     q_s(arr,low,pindex-1)
#     q_s(arr,pindex+1,high)

# def quick_sort(arr):
#   q_s(arr,0,len(arr)-1)
#   return arr


# arry = [13,24,20,9,46,52]
# n = len(arry)
# quick_sort(arry)
# print(arry)
  


