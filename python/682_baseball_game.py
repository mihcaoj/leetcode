# Time: O(n) / Space: O(n)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []

        for operation in operations:
            if operation.lstrip("-").isdigit():
                lst.append(int(operation))
            elif operation == 'C':
                lst.pop()
            elif operation == 'D':
                lst.append(2 * lst[-1])
            elif operation == '+':
                lst.append(lst[-1] + lst[-2])
        return sum(lst)
