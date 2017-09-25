import sys
import os

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail

def removeNodes(list, x):
    # init link list
    if len(list) > 0:
        h = LinkedListNode(list[0])
        t = h
        for v in list[1:]:
            t =  _insert_node_into_singlylinkedlist(h, t, v)     
    else:
        return None
    
    # return h
    pointer = h
    while (pointer.next != None):
        if (pointer.next.val > x):
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next

    if h.val > x:
        return h.next
    else:
        return h
   


h = removeNodes([9,1,2,5,9,10,90],3)
print(h.val)
while h.next != None:
    print (h.next.val)
    h = h.next







    