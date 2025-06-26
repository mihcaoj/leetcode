'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
'''
class Solution:
    # Time: O(n) / Space: O(1)
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for char in columnTitle:
            # integer code point, normalize to 0, add 1 to make it 1-based instead of 0-based
            val = ord(char) - ord('A') + 1
            res = res * 26 + val
        return res
