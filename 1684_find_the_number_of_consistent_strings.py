'''
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
'''
class Solution:
    # Time: O(n*m) / Space: O(1)
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        count = 0
        for word in words:
            if all(char in allow for char in word):
                count += 1
        return count
