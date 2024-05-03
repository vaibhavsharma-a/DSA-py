class Node:
  def __init__(self,data,next_node=None,prev_node=None):
    self.data = data
    self.next = next_node
    self.prev = prev_node

def convertarraytoDLL(arr):
  head = Node(arr[0])
  prev = head

  for i in range(1,len(arr)):
    temp = Node(arr[i],None,prev)

    prev.next = temp

    prev = temp
  
  return head


def print_list(head):
  while head is not None:
    print(head.data, end=" ")

    head = head.next

def deleltehead(head):
  if head == None or head.next == None:
    return None

  prev = head
  head = head.next
  head.prev = None
  prev.next = None
  return head

def deletetail(head):
  if head == None or head.next == None:
    return None
  
  tail = head
  while tail.next != None:
    tail = tail.next

  prev = tail.prev
  prev.next = None
  tail.prev = None

  return head

def removetheknode(head,k):
  if head is None:
    return None
  
  knode = head
  cnt = 0

  while knode != None:
    cnt += 1
    if cnt == k:
      break
    knode = knode.next

  back = knode.prev
  front = knode.next

  if back is None and front is None:
    return None
  
  elif back is None:
    return deleltehead(head)
  
  elif front is None:
    return deletetail(head)
  
  back.next = front
  front.prev = back

  knode.next = None
  knode.prev = None

  del knode
  return head
    

def deletethegivennode(node):
  
  prev = node.prev
  front = node.next

  if front == None:
    prev.next = None
    node.prev = None
    del node
    return
  
  prev.next = front
  front.prev = prev

  node.next = None
  node.prev = None

  del node

def insertbeforehead(head,val):

  before = Node(val,head)
  
  head.prev = before
  return before

def insertbeforetail(head,val):
  if head.next == None:
    return insertbeforehead(head,val)
  
  temp = head
  while temp.next is not None:
    temp = temp.next
  
  back = temp.prev
  beforetail = Node(val,temp,back)
  back.next = beforetail
  temp.prev = beforetail

  return head

def insertbeforekthnode(head,val,k):
  if k == 1:
    return insertbeforehead(head,val)

  temp = head
  cnt = 0
  while temp.next is not None:
    cnt += 1
    if cnt == k:
      break
    temp = temp.next
  
  back = temp.prev
  added = Node(val,temp,back)
  back.next = added
  temp.prev = added

  return head

def insertbeforegivenode(head,node,val):
  
  temp = head
  while temp.next is not None:
    if temp.data == node:
      break
    temp = temp.next

  back = temp.prev
  added = Node(val,temp,back)
  back.next = added
  temp.prev = added

  return head
def reverseaDLL(head):
  temp = head

  node_st = []

  while temp is not None:

    node_st.append(temp.data)

    temp = temp.next

  temp = head

  while node_st:

    temp.data = node_st.pop()

    temp = temp.next

  return head




arr = [2,3,5,6]
head = convertarraytoDLL(arr)
print_list(head)
print()
# head1 = deleltehead(head)
# print_list(head1)
# print()
# head2 = deletetail(head)
# print_list(head2)
# khead = removetheknode(head,1)
# print_list(khead)
# deletethegivennode(head.next.next.next)
# print_list(head)
# new_head = insertbeforehead(head,12)
# print_list(new_head)
# new_head = insertbeforetail(head,15)
# print_list(new_head)
# new_head = insertbeforekthnode(head,12,2)
# print_list(new_head)
# new_node = insertbeforegivenode(head,5,18)
# print_list(new_node)
# revhed = reverseaDLL(head)
# print_list(revhed)