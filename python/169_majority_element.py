class Solution:
    # Time: O(n) / Space: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        my_map = {}

        for num in nums:
            if num in my_map:
                my_map[num] += 1
            else:
                my_map[num] = 1
        majority_element = max(my_map, key=my_map.get)
        return majority_element

    # Boyer–Moore Algorithm (Time: O(n) / Space: O(1))
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
