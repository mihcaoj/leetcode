'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.
'''
class Solution:
    # Time: O(1) / Space: O(1)
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
