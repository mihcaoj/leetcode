'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid.
If there is no island, return 0.
'''
class Solution:
    # Time: O(n*m) / Space: O(n*m)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols): return 0
            if grid[r][c] == 0: return 0

            grid[r][c] = 0
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    curr_area = dfs(r, c)
                    max_area = max(curr_area, max_area)
        return max_area
