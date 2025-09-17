# Time: O(n) / Space: O(n)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(w for w in words if w not in banned_set)
        return count.most_common(1)[0][0]
