class Solution:
    # Time: O(n) / Space: O(n)
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c.values())
