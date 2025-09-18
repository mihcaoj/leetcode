# Time: O(b+n*m) / Space: O(b+m)
class Solution:
    def canBeTypedWords(self, text: str, broken_letters: str) -> int:
        words = text.split()
        broken = set(broken_letters)
        count = 0

        for word in words:
            if not (set(word) & broken):
                count += 1
        return count
