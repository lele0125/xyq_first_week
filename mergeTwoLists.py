class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = ListNode(0)
        p = result
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        p.next = l1 if l1 else l2
        return result.next
