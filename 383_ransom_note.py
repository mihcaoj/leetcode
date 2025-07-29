class Solution:
    # Time: O(n+m) / Space: O(1)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        magazine = Counter(magazine)

        return ransom <= magazine

    # Using only one counter (Time: O(n+m) / Space: O(1))
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for char in ransomNote:
            if count[char] == 0:
                return False
            count[char] -= 1
        return True
