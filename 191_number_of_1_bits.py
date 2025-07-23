'''
Given a positive integer n, write a function that returns the number of in its binary representation (also known as the Hamming weight).
'''
class Solution:
    # Time: O(n) / Space: O(1)
    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0

        for bit in bin(n)[2:]:
            if bit == '1':
                hamming_weight += 1
        return hamming_weight
