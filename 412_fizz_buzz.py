class Solution:
    # Time: O(n) / Space: O(n)
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n+1)]

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i-1] = "Fizz"
            elif i % 5 == 0:
                answer[i-1] = "Buzz"
        return answer

    # Cleaner solution (Time: O(n) / Space: O(n))
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
