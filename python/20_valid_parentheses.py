# Time: O(n) / Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if char == ')' and popped != '(':
                    return False
                elif char == '}' and popped != '{':
                    return False
                elif char == ']' and popped != '[':
                    return False

        return len(stack) == 0

# Map solution (Time: O(n) / Space: O(n))
    def isValid2(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
