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
class Node:
  def __init__(self,data)-> None:
    self.data = data
    self.next = None

# create a single linked list class
class SinglyLL:
  def __init__(self)-> None:
    self.head = None

  # creating function for traversal in the linked list
  def traversal(self) -> None:
    if self.head is None:
      print("This singly linkded list is empty")
    else:
      a = self.head
      while a is not None:
        print(a.data, end = " ")
        a=a.next
  # insert the data at the beggining
  def insert_at_beg(self,data):
    print()
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_last(self,data):
    print()
    new_node = Node(data)
    a = self.head
    while a.next is not None:
      a=a.next
    a.next = new_node

  def insert_at_spes_pos(self,pos,data):
    print()
    nib = Node(data)
    a = self.head
    for _ in range(1,pos-1):
      a = a.next
    nib.next = a.next
    a.next = nib 

  def delete_the_node_at_start(self):
    print()
    a = self.head
    self.head = a.next
    a.next = None

  def delete_the_node_at_end(self):
    print()
    prev = self.head
    a = self.head.next
    while a.next is not None:
      prev = prev.next
      a = a.next
    prev.next = None

  def del_at_specs_node(self,pos): 
    print()
    prev = self.head
    a = self.head.next
    for _ in range(1,pos-1):
      prev = prev.next
      a = a.next
    prev.next = a.next
    a.next = None




sll = SinglyLL()
n1 = Node(10)
sll.head = n1
n2 = Node(13)
n1.next= n2
n3 = Node(130)
n2.next = n3
n4 = Node(25)
n3.next = n4
n5 = Node(36)
n4.next= n5
sll.traversal()
sll.insert_at_beg(67)
sll.traversal()
sll.insert_at_last(200)
sll.traversal()
sll.insert_at_spes_pos(2,666)
sll.traversal()
sll.delete_the_node_at_start()
sll.traversal()
sll.delete_the_node_at_end()
sll.traversal()
sll.del_at_specs_node(3)
sll.traversal()
