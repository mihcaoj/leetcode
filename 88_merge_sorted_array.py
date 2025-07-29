class Solution:
    # Time: O(n+m) / Space: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2: return

        p1 = m - 1 # last elem of nums1
        p2 = n - 1 # last elem of nums2
        p = m + n - 1 # last index of nums1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
