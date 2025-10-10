class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        heap = []
        for i in range(n):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][m - 1], i, m - 1))
            visited[i][0] = True
            visited[i][m - 1] = True
        for j in range(1, m - 1): 
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[n - 1][j], n - 1, j))
            visited[0][j] = True
            visited[n - 1][j] = True
        water = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    neighbor_height = heightMap[nx][ny]
                    water += max(0, height - neighbor_height)
                    heapq.heappush(heap, (max(height, neighbor_height), nx, ny))
        return water