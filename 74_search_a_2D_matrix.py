'''
You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    # Time: O(logm+logn) / Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, up = 0, 0
        right, down = len(matrix) - 1, len(matrix) - 1

        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                top = mid + 1

        row = (up + down) // 2

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
