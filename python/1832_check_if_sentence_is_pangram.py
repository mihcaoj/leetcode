# Time: O(n) / Space: O(1)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        my_set = set(sentence)

        for i in my_set:
            alphabet.remove(i)

        if alphabet == []:
            return True
        else:
            return False
