'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        return goal in s + s
