from typing import List


class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * n
        out_degree = [0] * n
        for a, b in trust:
            out_degree[a - 1] += 1
            in_degree[b - 1] += 1
        for i in range(n):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i + 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    trust = [[1, 2], [2, 3], [1, 3]]
    n = 3
    output = solution.findJudge(n=n, trust=trust)
    print(output)
