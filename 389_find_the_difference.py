class Solution:
    # Time: O(s+t) / Space: O(1)
    def findTheDifference(self, s: str, t: str) -> str:
        if not s: return t

        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)
