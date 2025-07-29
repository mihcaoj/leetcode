class Solution:
    # Time: O(n) / Space: O(n)
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
