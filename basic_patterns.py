for i in range(1,6):
  for j in range(1,6):
    print("*",end=" ")
  print()
print("--------------------------------")
for i in range(1,6):
  for j in range(1,i+1):
    print("*",end=" ")
  print()
print("--------------------------------")
for i in range(1,6):
  for j in range(1,i+1):
    print(j,end=" ")
  print()
print("--------------------------------")
for i in range(1,6):
  for j in range(1,i+1):
    print(i,end=" ")
  print()
print("--------------------------------")
for i in range(5,0,-1):
  for j in range(1,i+1):
    print("*",end = " ")
  print()
print("--------------------------------")
for i in range(5,0,-1):
  for j in range(i,0,-1):
    print(j,end = " ")
  print()
print("--------------------------------")
for i in range(5,0,-1):
  for j in range(1,i+1):
    print(j,end = " ")
  print()
print("--------------------------------")
rows =5
for i in range(rows):
  print(" " * (rows-i-1) + "*" * (2*i+1))
# print("--------------------------------")
for i in range(rows):
  for j in range(i):
    print(" ",end="")
  for k in range(2*(rows-i)-1):
    print("*",end="")
  print()
print("--------------------------------")
for i in range((2*rows)-1):
  if i < rows:
    for j in range(i+1):
      print("*",end= "")
  else:
    for j in range(rows*2 - 1 - i):
      print("*",end="")
  print()
print("--------------------------------")
start = 1
for i in range(0,5):
  if i%2 == 0:
    start = 1
  else:
    start = 0
  for j in range(i+1):
    print(start,end=" ")
    start = 1 - start
  print()
print("__________________")
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(j, end="")

  for k in range(2*rows - 2*i):
    print(" ",end="")

  for l in range(i,0,-1):
    print(l,end="")
  print()
print("_________________________")
for i in range(1,6):
  for j in range(65,65+i):
    print(chr(j), end=" ")
  print()

print("_________________________")
for i in range(5,0,-1):
  for j in range(65,65+i):
    print(chr(j), end=" ")
  print()
print("____________________________")
for i in range(5):
  for j in range(i+1):
    print(chr(65+i),end=" ")
  print()
print("_____________________")
num = 5
for i in range(num):
  print(" " * (num-i-1),end="")

  for j in range(i+1):
    print(chr(65+j),end="")

  for j in range(i,0,-1):
    print(chr(65+j-1),end="")
  print()
print("-------------------------")
num = 5
for i in range(num):
  for j in range(69-i,70):
      print(chr(j),end=" ")
  print()
print("-------------------------")
num = 4
for i in range(num):
  
  for j in range(0,num-i):
    print("*",end="")
  
  for s in range(2*i):
    print(" ",end="")

  for j in range(0,num-i):
    print("*",end="")
  print()

for i in range(1,num+1):
  for j in range(0,i):
    print("*",end="")

  for s in range(2*(num-i)):
    print(" ",end="")

  for j in range(0,i):
    print("*",end="")
  print()
    
print("-------------------------")
for i in range(1,num+1):
  for j in range(0,i):
    print("*",end="")

  for s in range(2*(num-i)):
    print(" ",end="")

  for j in range(0,i):
    print("*",end="")
  print()

for i in range(num-1,0,-1):
  for j in range(0,i):
    print("*",end="")

  for s in range(2*(num - i)):
    print(" ",end="")


  for j in range(0,i):
    print("*",end="")
  print()
print("__________________")  
for i in range(0,7):
  for j in range(0,4):
    if i%2 == 0:
      if i%3==0:
        print("*", end=" ")
      elif j==0 or j==3:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    else:
      print(" ", end=" ")
  print()
print("________________________")
for i in range(num):
  for j in range(num):
    if i == 0 or i == num - 1 or j == 0 or j == num-1:
      print("*", end=" ")
    else: 
      print(" ",end=" ")
  print()
print("________________________")

for i in range(0,2*num - 1):
  for j in range(0,2*num - 1):
    top = i
    left = j 
    right =  (2*num - 2) - j
    bottom =  (2*num - 2) - i
    print(num - min(min(top,bottom),min(left,right)),end="")

  print()



