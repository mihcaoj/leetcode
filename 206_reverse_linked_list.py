class Solution:
    # Iterative solution (Time: O(N) / Space: O(1))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        current = head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    # Recursive solution (Time: O(N) / Space: O(N))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if head is None:
          return prev

       next = head.next
       head.next = prev
       return self.reverseList(next, head)
