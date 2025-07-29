class Solution:
    # Time: O(n) / Space: O(1)
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, col = 0, 0
        for command in commands:
            if command == "DOWN":
                row += 1
            elif command == "UP":
                row -= 1
            elif command == "RIGHT":
                col += 1
            elif command == "LEFT":
                col -= 1
        return (row * n) + col
