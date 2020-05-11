class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if N == 1 and len(trust) == 0:
            return 1
        trusted_num = [0 for _ in range(N + 1)]
        trusting_num = [0 for _ in range(N + 1)]
        for i in trust:
            trusted_num[i[1]] += 1
            trusting_num[i[0]] += 1
        for key, j in enumerate(trusted_num):
            if j == N-1 and trusting_num[key] == 0:
                return key
        return -1