class Solution:
    # Time: O(n) / Space: O(n)
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable_mountains = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                stable_mountains.append(i)
        return stable_mountains

    # List comprehension one liner (Time: O(n) / Space: O(n))
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]
