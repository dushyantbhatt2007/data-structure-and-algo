from typing import List


class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [True] + [False] * (len(rooms) - 1)
        stack = [0]
        while stack:
            cur = stack.pop()
            for room in rooms[cur]:
                if not visited[room]:
                    visited[room] = True
                    stack.append(room)
        return all(visited)


if __name__ == "__main__":
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    solution = Solution()
    output = solution.canVisitAllRooms(rooms)
    print(output)
