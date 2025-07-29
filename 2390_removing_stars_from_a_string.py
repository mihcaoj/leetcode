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
