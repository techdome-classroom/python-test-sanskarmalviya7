class Solution:
    def explore_island(self, grid, row, col, visited):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited[row][col] = True

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 'L' and not visited[new_row][new_col]:
                self.explore_island(grid, new_row, new_col, visited)

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and not visited[i][j]:
                    self.explore_island(grid, i, j, visited)
                    island_count += 1

        return island_count
