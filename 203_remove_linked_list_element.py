class Solution:
    # Time: O(N) / Space: O(1)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next
