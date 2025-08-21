class Solution:
    # Time: O(n) / Space: O(n)
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = [[] for _ in range(len(groupSizes) + 1)]
        solution = []

        for i, size in enumerate(groupSizes):
            buckets[size].append(i)

            if len(buckets[size]) == size:
                solution.append(buckets[size])
                buckets[size] = []

        return solution
