'''
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
'''
class Solution:
    # Dict solution (Time: O(n) / Space: O(n))
    def firstUniqChar(self, s: str) -> int:
        char_count = {}

        # Count
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Find index of first char in string
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        # No unique char found
        return -1

    # Counter solution (Time: O(n) / Space: O(n))
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
