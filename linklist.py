"""singly linked list"""

# class Node:
#   def __init__(self,data)->None:
#     self.data = data
#     self.next = None

# n1 = Node(89)
# print(n1.data)
# print(n1.next)
    
# class singlyLL:
#   def __init__(self) -> None:
#     self.head = None

"""traversal throught the linked list"""
# make a node class
# class Node:
#   def __init__(self,data)-> None:
#     self.data = data
#     self.next = None

# # create a single linked list class
# class SinglyLL:
#   def __init__(self)-> None:
#     self.head = None

#   # creating function for traversal in the linked list
#   def traversal(self) -> None:
#     if self.head is None:
#       print("This singly linkded list is empty")
#     else:
#       a = self.head
#       while a is not None:
#         print(a.data, end = " ")
#         a=a.next
#   # insert the data at the beggining
#   def insert_at_beg(self,data):
#     print()
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head = new_node

#   def insert_at_last(self,data):
#     print()
#     new_node = Node(data)
#     a = self.head
#     while a.next is not None:
#       a=a.next
#     a.next = new_node

#   def insert_at_spes_pos(self,pos,data):
#     print()
#     nib = Node(data)
#     a = self.head
#     for _ in range(1,pos-1):
#       a = a.next
#     nib.next = a.next
#     a.next = nib 

#   def delete_the_node_at_start(self):
#     print()
#     a = self.head
#     self.head = a.next
#     a.next = None

#   def delete_the_node_at_end(self):
#     print()
#     prev = self.head
#     a = self.head.next
#     while a.next is not None:
#       prev = prev.next
#       a = a.next
#     prev.next = None

#   def del_at_specs_node(self,pos): 
#     print()
#     prev = self.head
#     a = self.head.next
#     for _ in range(1,pos-1):
#       prev = prev.next
#       a = a.next
#     prev.next = a.next
#     a.next = None




# sll = SinglyLL()
# n1 = Node(10)
# sll.head = n1
# n2 = Node(13)
# n1.next= n2
# n3 = Node(130)
# n2.next = n3
# n4 = Node(25)
# n3.next = n4
# n5 = Node(36)
# n4.next= n5
# sll.traversal()
# sll.insert_at_beg(67)
# sll.traversal()
# sll.insert_at_last(200)
# sll.traversal()
# sll.insert_at_spes_pos(2,666)
# sll.traversal()
# sll.delete_the_node_at_start()
# sll.traversal()
# sll.delete_the_node_at_end()
# sll.traversal()
# sll.del_at_specs_node(3)
# sll.traversal()

#! we need to write the function for converting array to a link list before runing any other

class Node:
  def __init__(self,data,next=None)->None:
    self.data = data
    self.next = next
  
  
    
def print_list(head):
  while head is not None:
    print(head.data,end=" ")
    head = head.next
  print()

#! convert an array to linked list
def converttoLL(arr):
  n = len(arr)
  head = Node(arr[0])
  mover = head
  for i in range(1,n):
    temp = Node(arr[i])
    mover.next = temp
    mover = temp
  return head

def deletehead(head):
  # temp = head
  # temp = temp.next
  # head.next = None
  # return temp
  return head.next

def deltail(head):
  temp = head
  prev = None
  while temp.next is not None:
    prev = temp
    temp = temp.next
  
  prev.next = None
  return head

# #! delete at a specific position
def deleteK(head,k):
  if head == None:
    return head
  if k == 1:
    # temp = head
    # head = head.next
    # temp.next = None
    # return head
    return deletehead(head)
  cnt = 0
  temp = head
  prev = None
  while temp != None:
    cnt += 1
    if cnt == k:
      prev.next = prev.next.next
      temp.next = None
      break
    prev = temp
    temp = temp.next
  return head
  
# #! delete the node with given element

def deletelm(head,elm):
  if head == None:
    return head
  if head.data == elm:
    # temp = head
    # head = head.next
    # temp.next = None
    # return head
    return deletehead(head)
  temp = head
  prev = None
  while temp is not None:
    if temp.data == elm:
      prev.next = prev.next.next
      temp.next = None
      break
    prev = temp
    temp = temp.next
  return head

# #! insertion in the LL

# #? insert at the start of the LL

# def insertinthestart(list: Node,newval:int):
#   # head = list
#   temp = Node(newval,list)
#   # temp.next = head
#   return temp

def insertionhead(head,newval):
  return Node(newval,head)


# #! insert at the last
# def insertattail(head,val):
#   if head == None:
#     return Node(val)
#   temp = head
#   tail = Node(val)
#   while temp.next != None:
#     temp = temp.next
#   temp.next = tail
#   return head

def tailinsertion(head,val):
  temp = head
  
  while temp.next is not None:
    
    temp = temp.next

  newnode = Node(val)
  temp.next = newnode
  return head

# #! insert at Kth postion (k -> 1 to N+1)
  
# def insertnodeatk(head,k,el):
#   if head is None:
#     if k == 1:
#       return Node(el)
#     else:
#       return "This can't be done"
  
#   if k == 1:

#     temp = Node(el,head)
#     return temp
  
#   cnt = 0
#   temp = head
#   while temp is not None:
#     cnt += 1
#     if cnt == k-1:
#       new_node = Node(el) #? this can also be written as new_node = Node(el,temp.next), so we can remove next step 
#       new_node.next = temp.next
#       temp.next = new_node
#       break
#     temp = temp.next

#   return head

def insertatk(head,k,val):
  if head is None:
    if k == 1:
      return Node(val)
    
  if k == 1:
    return insertionhead(head,val)
  
  temp = head
  cnt = 0
  prev = None
  while temp.next is not None:
    cnt += 1
    if cnt == k:
      newnode = Node(val,temp)
      prev.next = newnode
      break
    prev = temp
    temp = temp.next

  return head



# #! insert before a certain value in a linked list

# def insertbeforeval(head,el,val):
#   if head is None:
#     return None
  
#   if head.data == val:
#     new_node = Node(el,head)
#     return new_node
  
#   temp = head
#   while temp.next is not None:
#     if temp.next.data == val:
#       new_node = Node(el,temp.next)
#       temp.next = new_node
#       break
  
#     temp = temp.next

#   return head

def insert_bef_val(head,val,ins):

  if head is None:
    return None
  if head.data == val:
    return Node(ins,head)
  
  temp = head
  prev = None
  while temp.next is not None:
    if temp.data == val:
      newnode = Node(ins,temp)
      prev.next = newnode
      break
    prev = temp
    temp = temp.next

  return head

def checkforloop(head):
  temp = head
  check ={}

  while temp is not None:
    if temp in check:
      return "Yes there is a loop"
    
    check[temp] = 1
    print(check)

    temp = temp.next
  return "there is not loop in the list"

def revlist(head):
  temp = head
  prev = None
  while temp is not None:
    front = temp.next
    temp.next = prev
    prev = temp
    temp = front
  return prev

def oddeven(head):
  arr = []
  temp = head
  while temp is not None and temp.next is not None:
    arr.append(temp.data)
    temp = temp.next.next
  
  if temp:
    arr.append(temp.data)

  temp = head.next
  while temp is not None and temp.next is not None:
    arr.append(temp.data)
    temp = temp.next.next
  
  if temp:
    arr.append(temp.data)
  
  i = 0 
  temp = head
  while temp is not None:
    temp.data = arr[i]
    i+= 1
    temp = temp.next
  
  return head

def evenoddopti(head):
  odd = head
  even = head.next
  even_node = head.next

  if head is None or head.next is None:
    return head
  
  while even is not None and even.next is not None:
    odd.next = odd.next.next
    even.next = even.next.next

    odd = odd.next
    even = even.next

  odd.next = even_node

  return head


def sort_list_of_0_1_2(head):
  cnt0,cnt1,cnt2 = 0,0,0
  temp = head

  while temp is not None:
    if temp.data == 0:
      cnt0+=1
    elif temp.data == 1:
      cnt1 += 1
    else:
      cnt2 += 1
    
    temp = temp.next
  
  temp = head
  while temp is not None:
    if cnt0:
      temp.data = 0
      cnt0 -= 1
    elif cnt1:
      temp.data = 1
      cnt1 -= 1
    else:
      temp.data = 2
      cnt2 -= 1

    temp = temp.next

  return head

def sort_0_1_2(head):
  zero_head = Node(-1)
  one_head = Node(-1)
  two_head = Node(-1)
  
  zero = zero_head
  one = one_head
  two = two_head

  temp = head

  while temp is not None:
    if temp.data == 0:
      zero.next = temp
      zero = temp
    
    elif temp.data == 1:
      one.next = temp
      one = temp
    
    else:
      two.next = temp
      two = temp
    
    temp = temp.next

  if one_head.next:
    zero.next = one_head.next
  else:
    zero.next = two_head.next

  one.next = two_head.next
  two.next = None

  new_head = zero_head.next

  return new_head

def add1_to_ll(head):

  head = revlist(head)
  temp = head
  carry = 1

  while temp is not None:

    temp.data = temp.data + carry
    if temp.data < 10:
      carry = 0
      break
    else:
      temp.data = 0
      carry = 1
    
    temp = temp.next
  
  if carry:
    new_node = Node(1)
    head = revlist(head)
    new_node.next = head
    return new_node
  
  head = revlist(head)
  return head



arr = [2,3,4,5,7,8]
arr012 = [0,2,1,2,1,0,2,1]
head1 = converttoLL(arr012)
# print_list(head1)
head = converttoLL(arr)
print_list(head)
add1 = [9,9,9]
added1 = converttoLL(add1)
# print()
# head1 = deletehead(head)
# print_list(head1)
# print()
# head3 = deltail(head)
# print_list(head3)
# print()
# head4 = deleteK(head,1)
# print_list(head4)
# print()
# head5 = deletelm(head,4)
# print_list(head5)
# headnew = insertionhead(head,22)
# print_list(headnew)
# headn = tailinsertion(head,55)
# print_list(headn)
# another_head = insertatk(head,4,666)
# print_list(another_head)
# lasthead = insert_bef_val(head,5,18)
# print_list(lasthead)
# print(checkforloop(head))
# reverse = revlist(head)
# print_list(reverse)
# print_list(head)
# head1 = evenoddopti(head)
# print_list(head1)
# head012 = sort_0_1_2(head1)
# print_list(head012)
print_list(added1)
headdy = add1_to_ll(added1)
print_list(headdy)
