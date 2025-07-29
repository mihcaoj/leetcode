class Solution:
    # Time: O(n+m) / Space: O(n+k)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        my_set = set(nums1)
        intersection = []

        for n in nums2:
            if n in my_set:
                intersection.append(n)
                my_set.remove(n)

        return intersection
