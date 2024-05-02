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
  while temp != None:
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


arr = [2,3,4,5,7]
head = converttoLL(arr)
print_list(head)
# print()
# head1 = deletehead(head)
# print_list(head1)
# print()
# head3 = deltail(head)
# print_list(head3)
print()
head4 = deleteK(head,1)
print_list(head4)