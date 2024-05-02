# name = input("Enter your name")

# def getlen(stin):
#   cnt = 0
#   for char in stin:
#     cnt += 1
#   return cnt

# def getlenwhile(stn):
#   cnt  = 0 
#   while stn:
#     cnt += 1
#     stn = stn[1:]
#   return cnt
    


# print(getlen(name))
# print(getlenwhile(name))

# stin = "hellow i am me"

# sting = stin.split(" ")
# rev = ""
# for i in range(len(sting)-1,-1,-1):
#   rev += sting[i] + " "
  



# print(rev)

# stin = input("Enter a name")
# n = len(stin)
# for i in range(1,n+1):
#   print(stin[-i],end="")

# print("\n--------------------")

# revstr = stin[::-1]
# print(revstr)

#! case conversion

# def tolower(char):
#   if ord(char) >= ord('a') and ord(char) <= ord('z'):
#     return char
#   else:
#     temp = ord(char) + 32
#     return chr(temp)
  
# print(tolower('M'))


# def toupper(char):
#   if ord(char) >= ord('A') and ord(char) <= ord('Z'):
#     return char
#   else:
#     temp = ord(char) - 32
#     return chr(temp)
  
# print(toupper('M'))


# strin = "a good   example"
# sti = strin.split()
# print(sti)
# strn = ""
# for i in range(len(sti)-1,-1,-1):
#   if sti[i] == " ":
#     continue
#   strn += sti[i] + " "


# print(strn.strip())


# sti = "obseqltttttttt"

# def getmaxoccr(sti):
#   feq = {}
#   for char in sti:
#     if char in feq:
#       feq[char] += 1
#     else:
#       feq[char] = 1

#   max_freq = -1
#   min_char = ''
    
#   for char, val in feq.items():
#     if val > max_freq or (val == max_freq and char < min_char):
#       max_freq = val
#       min_char = char

#   return min_char


# print(getmaxoccr("acccbbaba"))

# stri = "my name is vaibhav sharmna"

# temp = ""
# for i in range(0,len(stri)):
#   if stri[i] == " ":
#     temp += "@40"
#     pass
#   else:
#     temp += stri[i]
# print(temp)

# chars = ["i", " ", "a", "m", " ", "v", "i", "b", "h"]

# def reverse_word(chars):
#   temp = ""
#   for char in chars:
#     temp += char

#   print(temp)

#   temp = temp.split()
#   print(temp)
#   temp = temp[::-1]
#   print(temp)
#   temp = " ".join(temp)
#   print(temp)
#   temp_list = []
#   for char in temp:
#     temp_list.append(char)

#   return temp_list


# strin = "code is good aaa"

# temp = strin.split(" ")
# print(temp)
# temp = temp[::-1]
# print(temp)
# temp = " ".join(temp)
# print(temp)


# sting = '((0-9))(1-3)(((4+5)((0/2)(5-1)(5/9))(9-0)((4/3)(2+7))(3-6)(((6+2)))))'
# cnt = 0
# for i in sting:
#   if i == '(':
#     cnt += 1
  
# print(cnt)

# stin = "geeksforgeek"
# part = "e"
# index = stin.find(part)

# # stin = stin[:index] + stin[index+len(part):]
# # print(stin)
# # print(stin)
# while index != -1:
  
#   stin = stin[:index] + stin[index+len(part):]
#   index = stin.find(part)

# print(stin)


arr = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
frq = {}
for char in arr:
  if char not in frq:
    frq[char] = 1
  else:
    frq[char] += 1

ans = []
for char,times in frq.items():
  ans.append(char)
  if times == 1:
    continue
  elif times >= 10:
    sti = str(times)
    for char in sti:
      ans.append(char)

  else:
    ans.append(times)

print(ans)

# ans = str(12)
# print(type(ans))
# for dig in ans:
#   print(dig, end=" ")


