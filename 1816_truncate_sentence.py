'''
You are given a sentence s and an integer k.
You want to truncate s such that it contains only the first k words.
Return s after truncating it.
'''
class Solution:
    # Time: O(n) / Space: O(n)
    def truncateSentence(self, s: str, k: int) -> str:
        # This splits, slices the first k words, then joins them with spaces
        return ' '.join(s.split()[:k])
