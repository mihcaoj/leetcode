class Solution:
    # Time: O(n) / Space: O(n)
    def maximum69Number (self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                return int("".join(str(d) for d in digits))
        return num

    # One liner (Time: O(n) / Space: O(n))
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
