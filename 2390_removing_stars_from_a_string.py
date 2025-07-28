'''
You are given a string s, which contains stars *.
In one operation, you can:
- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
'''
class Solution:
    # Time: O(n) / Space: O(n)
    def removeStars(self, s: str) -> str:
        sol = []
        for i, char in enumerate(s):
            if char == '*':
                sol.pop()
            else:
                sol.append(char)
        return "".join(sol)
