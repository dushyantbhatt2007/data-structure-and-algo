from typing import List


class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        new_grid = [[0] * (2 * N) for _ in range(2 * N)]
        count = 0

        for i in range(N):
            for j in range(N):
                if grid[i][j] == '/':
                    new_grid[2 * i][2 * j + 1] = 1
                    new_grid[2 * i + 1][2 * j] = 1
                elif grid[i][j] == '\\':
                    new_grid[2 * i][2 * j] = 1
                    new_grid[2 * i + 1][2 * j + 1] = 1
        print(new_grid)

        def dfs(grid, i, j):
            # starting with a seed (0 in location i,j), build up an open space
            if grid[i][j] == 1:
                return
            grid[i][j] = 1  # mark as visited
            if i < len(grid) - 1:  # (make sure i+1 exists)
                dfs(grid, i + 1, j)  # search down
            if j < len(grid) - 1:
                dfs(grid, i, j + 1)  # search right
            if i > 0:
                dfs(grid, i - 1, j)  # search up
            if j > 0:
                dfs(grid, i, j - 1)  # search left
            # search dl
            if i < len(grid) - 1 and j > 0 and i % 2 == j % 2:
                dfs(grid, i + 1, j - 1)
            # search ur
            if i > 0 and j < len(grid) - 1 and i % 2 == j % 2:
                dfs(grid, i - 1, j + 1)
            # search dr
            if i < len(grid) - 1 and j < len(grid) - 1 and i % 2 != j % 2:
                dfs(grid, i + 1, j + 1)
            # search ul
            if i > 0 and j > 0 and i % 2 != j % 2:
                dfs(grid, i - 1, j - 1)

        # search for seeds (new islands)
        for i in range(2 * N):
            for j in range(2 * N):
                if new_grid[i][j] == 0:
                    count += 1
                    dfs(new_grid, i, j)  # seed an island

        return count


if __name__ == "__main__":
    solution = Solution()
    grid = [" /", "/ "]
    print(solution.regionsBySlashes(grid=grid))
