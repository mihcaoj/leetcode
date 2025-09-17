# Time: O(n) / Space: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        my_list = list(s)
        i, j = 0, len(s) - 1

        while (i < j):
            if my_list[i] in vowels and my_list[j] in vowels:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                i += 1
                j -= 1
            elif my_list[i] in vowels:
                j -= 1
            elif my_list[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(my_list)

# Time: O(n) / Space: O(1)
    def reverseVowels2(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = [char for char in s if char in vowels]
        result = []

        for char in s:
            if char in vowels:
                result.append(stack.pop())
            else:
                result.append(char)
        return "".join(result)
