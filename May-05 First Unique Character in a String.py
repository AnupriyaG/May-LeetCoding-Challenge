class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                res = i
                break
        return res