class Solution:
    # Time: O(1) / Space: O(1)
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32]
