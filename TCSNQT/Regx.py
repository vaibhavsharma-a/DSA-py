import re

# stin = "my name is vaibhav and i feel unlucky at times like 1 and 2 and 3 and this is true in most of the case"
# pat = r'and'

# ans = re.search(pat,stin)
# print(ans.group())

# str = "123vasy5"
# pattern = r'\d+'
# print(re.findall(pattern,stin))

# strin = "i love cricket, my fav player is rohit sharma"
# find = r"rohit sharma"
# rep = "virat kohli"
# print(re.sub(find,rep,strin))

# def checkval(paswed,shift):
#   long = len(paswed)
#   digit =  re.search(r'\d',paswed)
#   special = re.search(r'[@#$&!]',paswed)
#   uppr =  re.search(r'[A-Z]',paswed)
#   lower =  re.search(r'[a-z]',paswed)

#   if digit and special and uppr and lower and long>8:
#     sti = ""
#     for i in range(long):
#       ordi = ord(paswed[i])
#       number = ordi - shift
#       chrtr = chr(number)
#       sti += chrtr
#     print(sti)
#   else:print("ERROR!")



# checkval("UserF#123",3)

arr = [1,2,3,4,5,6]

def revarr(arr,m):
    first = arr[:m+1]
    second = arr[m+1:]

    second.reverse()

    result = first + second

    return result

def revar(arr,strt,end):
    while strt < end:
        arr[strt],arr[end] = arr[end],arr[strt]
        strt += 1
        end -= 1
    return arr
print(revar(arr,0,len(arr)-1))
print(revarr(arr,3))
