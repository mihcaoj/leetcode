'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''
class Solution:
    # Verbose solution, adaptable to +k instead of +1 only (Time: O(n) / Space: O(1))
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            result = digits[i] + carry
            if result < 10:
                digits[i] = result
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

    # Cleaner solution (Time: O(n) / Space: O(1))
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
