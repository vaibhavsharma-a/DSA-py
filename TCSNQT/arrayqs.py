
#! 1 Find smallest number in an array


def smallerstnum(arr):
  n = len(arr)
  smallest = float("inf")
  for i in range(n):
    if arr[i] < smallest:
      smallest = arr[i]
  return smallest

#! 2 find largest number

def largestnum(arr):
  n = len(arr)
  large = -float('inf')
  for i in range(n):
    if arr[i] > large:
      large = arr[i]

  return large

#! 3 second smallest

def secondsmall(arr):
  if len(arr)<2:
    return -1 
  smallest = float('inf')
  second_small = float('inf')
  for i in range(len(arr)):
    if arr[i] < smallest:
      second_small = smallest
      smallest = arr[i]
    elif arr[i] < second_small and arr[i] != smallest:
      second_small = arr[i]
  return second_small

#! 4 second largest
def secondlarge(arr):
  if len(arr) < 2:
    return -1
  larget = -float('inf')
  secondlar = -float('inf')
  for i in range(len(arr)):
    if arr[i] > larget:
      secondlar = larget
      larget = arr[i]
    elif arr[i] > secondlar and arr[i] != larget:
      secondlar = arr[i]
  return secondlar

#! 5 rev an array
def revarray(arr):
  # return arr[::-1]
  n = len(arr)
  lef = 0
  right = n-1
  while lef < right:
    arr[lef],arr[right] = arr[right],arr[lef]
    lef+=1
    right -= 1
  return arr

#! 6 print freq of array elements
def freqency(arr):
  count = {}
  for val in arr:
    if val in count:
      count[val] += 1
    else:
      count[val] = 1
  for val,times in count.items():
    print(f"The element {val} is occuring {times} times in the array")

#! print in acending and decending order

def increasedecrease(arr):
  arr.sort()
  n = len(arr)
  for i in range(n//2):
    print(arr[i],end=" ")
  for i in range(n-1,n//2-1,-1):
    print(arr[i],end=" ")

#! median of an array

def getmed(arr):
  arr.sort()
  n = len(arr)
  if n%2 == 0:
    ind1 = (n//2)-1
    ind2 = (n//2)
    print(f"median of the array is {(arr[ind1]+arr[ind2])/2}")
  else:
    print(f"median of the array is {arr[n//2]}")

#! romve dupli from sorted
def removeduplicatesorted(arr):
  #? not in place in the given array
  # check = {}
  # for i in range(len(arr)):
  #   if arr[i] not in check:
  #     check[arr[i]] = 1
  #   else:
  #     check[arr[i]] += 1
  # for val in check.keys():
  #   print(val,end=" ")
  st = set()
  n = len(arr)
  for i in range(n):
    st.add(arr[i])
  
  k = len(st)
  j = 0
  for x in st:
    arr[j] = x
    j += 1
  return k
#! remove dupli from unsorted
def removedupunsort(arr):
  maping = {}
  for i in range(len(arr)):
    if arr[i] not in maping:
      print(arr[i],end=" ")
      maping[arr[i]] = 1

def insertabegin(arr,number):
  arr.append(None)
  n = len(arr)
  for i in range(n-1,0,-1):
    arr[i] = arr[i-1]
  arr[0] = number
  return arr
  
def insertatpos(arr,pos,val):
  arr.append(None)
  n = len(arr)
  for i in range(n-1,pos-1,-1):
    arr[i] = arr[i-1]

  arr[pos-1] = val
  return arr

def maxsubprod(arr):
  n = len(arr)
  ans = -float('inf')
  pre,suff = 1,1
  for i in range(n):
    if pre == 0:
      pre = 1
    if suff == 0:
      suff = 1
    pre = pre*arr[i]
    suff = suff*arr[n-i-1]
    ans = max(ans,max(pre,suff))
  return ans

#! to find max sub array sum
def kdanalgo(arr):
  sum = 0
  max_sum = float('-inf')
        
  for i in range(len(arr)):
    sum += arr[i]

    if sum > max_sum:
      max_sum = sum
    
    if sum < 0:
      sum = 0
  
  if max_sum < 0:
    max_sum = 0
  
  return max_sum
    
#! replace the elmenet by rank
def displayviarank(arr):
  n = len(arr)
  place = {}
  temp = 1
  arenew = [0]*n
  for i in range(n):
    arenew[i] = arr[i]
  
  arenew.sort()
  print(arenew)

  for i in range(n):
    
    if arenew[i] not in place:
      place[arenew[i]] = temp
      temp += 1

  for i in range(n):
    print(place[arr[i]],end=" ")

#! Print the element based on the fequency

def pritfreq(arr):
  count = {}
  n = len(arr)
  for i in range(n):
    if arr[i] not in count:
      count[arr[i]] = 1
    else:
      count[arr[i]] += 1

  print(count)
  sorted_count = sorted(count.items(),key=lambda x : x[1])
  print(sorted_count)

# arr=[1,2,1,2,2,3,3,4]
# pritfreq(arr)

#! rotate to left or right

def reverse(arr,start,end):
  while start <= end:
    arr[start],arr[end] = arr[end],arr[start]
    start += 1
    end -= 1
  

def rotatelefrright(arr,n,k):

  reverse(arr,0,n-k-1)
  reverse(arr,n-k,n-1)
  reverse(arr,0,n-1)

  return arr

def equilibriumindex(arr,n):
  total =  sum(arr)
  lsum = 0
  rsum = total

  for i in range(n):
    rsum -= arr[i]
    if rsum == lsum:
      return i
    lsum += arr[i]
  
  return -1

def close_integer(X,Y):
  
  mod =  X % Y
  if mod == 1:
    return X - 1
  elif mod == 0:
    return X
  elif mod < Y//2:
    
    return X - mod
  else:
    diff = Y-mod
    return X+diff


    

if __name__ == "__main__":
  arr = [12,43,23,5,67,42]
  arr1 = [1,2,3,2,3,1,2,3,4,5,3,2]
  arr3 = [2,6,1,7,9,5,4]
  arr4 = [2,5,1,7]
  arr5 = [1,1,1,2,2,3,3,4,5]
  arr6 = [1,2,-3,0,-4,-5]
  arr7 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  arr8 = [2,3,5,6,7,9]
  n = len(arr8)
  arr9 = [1,-1,2]
  n1 = len(arr9)
  # print(smallerstnum(arr))
  # print(largestnum(arr))
  # print(secondsmall(arr))
  # print(secondlarge(arr))
  # print(revarray(arr))
  # freqency(arr1)
  # increasedecrease(arr3)
  # getmed(arr4)
  # val = removeduplicatesorted(arr5)
  # for i in range(val):
  #   print(arr5[i],end=" ")
  # arr6 = [4, 3, 9, 2, 4, 1, 10, 89, 34]
  # removedupunsort(arr6)
  # print(insertabegin(arr,89))
  # print(insertatpos(arr,3,666))
  # print(maxsubprod(arr6))
  # print(kdanalgo(arr7))
  # displayviarank(arr8)
  # print(reverse(arr8,0,len(arr8)-1))
  # print(rotatelefrright(arr8,n,2))
  # print(equilibriumindex(arr9,n1))
  print(close_integer(13,4))


  

  

  
