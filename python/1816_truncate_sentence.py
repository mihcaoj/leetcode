class Solution:
    # Time: O(n) / Space: O(n)
    def truncateSentence(self, s: str, k: int) -> str:
        # This splits, slices the first k words, then joins them with spaces
        return ' '.join(s.split()[:k])
