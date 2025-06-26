'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
'''
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
