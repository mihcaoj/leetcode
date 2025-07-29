class Solution:
    # Time: O(n+m) / Space: O(m)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelz = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewelz:
                count += 1
        return count
