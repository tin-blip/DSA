# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        values = []

        for l in lists:
            while l:
                values.append(l.val)
                l = l.next

        values.sort()

        dummy = ListNode(0)
        current = dummy

        for v in values:
            current.next = ListNode(v)
            current = current.next

        return dummy.next
