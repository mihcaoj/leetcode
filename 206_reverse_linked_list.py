'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
class Solution:
    # Iterative solution (Time: O(n) / Space: O(1))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    # Recursive solution (Time: O(n) / Space: O(n))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if head is None:
          return prev

       next = head.next
       head.next = prev
       return self.reverseList(next, head)
