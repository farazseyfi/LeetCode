class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # Create a dummy node to handle the case where the head itself is a duplicate
        dummy.next = head
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next
