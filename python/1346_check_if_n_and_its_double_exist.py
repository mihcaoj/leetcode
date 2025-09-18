class Solution:
    # Brute force solution (Time: O(n^2) / Space: O(1))
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True
        return False

    # Set solution (Time: O(n) / Space: O(n))
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
