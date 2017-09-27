# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            prev = head
            cur = head.next
            head.next = None
            head = cur
            while cur.next:
                # jump to next
                cur = cur.next
                # redirect pinter
                head.next  = prev
                prev = head
                head = cur
            head.next = prev
        return head
    


class Solution2:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev