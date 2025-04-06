from heapq import heappop, heappush
from typing import List


# Sorting Queries + Min-Heap Expansion
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rowCount, colCount = len(grid), len(grid[0])
        result = [0] * len(queries)
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Sắp xếp queries để xử lý theo thứ tự tăng dần
        sortedQueries = sorted(enumerate(queries), key=lambda x: x[1])
        
        # Min-heap lưu trữ (giá trị ô, tọa độ hàng, cột)
        minHeap = [(grid[0][0], 0, 0)]
        visited = [[False] * colCount for _ in range(rowCount)]
        visited[0][0] = True
        totalPoints = 0
        
        for queryIndex, queryValue in sortedQueries:
            while minHeap and minHeap[0][0] < queryValue:
                cellValue, r, c = heappop(minHeap)
                totalPoints += 1
                
                # Duyệt 4 hướng
                for dr, dc in DIRECTIONS:
                    newRow, newCol = r + dr, c + dc
                    if 0 <= newRow < rowCount and 0 <= newCol < colCount and not visited[newRow][newCol]:
                        visited[newRow][newCol] = True
                        heappush(minHeap, (grid[newRow][newCol], newRow, newCol))
            
            result[queryIndex] = totalPoints
        
        return result
    


# Using Priority Queue with Binary Search
from queue import PriorityQueue

class Solution:
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def maxPoints(self, grid, queries):
        query_count = len(queries)
        result = [0] * query_count
        row_count = len(grid)
        col_count = len(grid[0])
        total_cells = row_count * col_count

        threshold_for_max_points = [0] * (total_cells + 1)
        min_value_to_reach = [
            [float("inf")] * col_count for _ in range(row_count)
        ]

        min_value_to_reach[0][0] = grid[0][0]

        # Min-heap for processing cells in increasing order of their maximum
        # encountered value.
        min_heap = PriorityQueue()
        min_heap.put((grid[0][0], 0, 0))
        visited_cells = 0

        # Dijkstra's algorithm to compute minValueToReach for each cell
        while not min_heap.empty():
            current = min_heap.get()

            # Store the value required to reach `visitedCells` points.
            threshold_for_max_points[visited_cells + 1] = current[0]
            visited_cells += 1

            # Explore all possible directions.
            for direction in self.DIRECTIONS:
                new_row, new_col = (
                    current[1] + direction[0],
                    current[2] + direction[1],
                )

                # Check if the new position is within bounds and not visited
                # before.
                if (
                    0 <= new_row < row_count
                    and 0 <= new_col < col_count
                    and min_value_to_reach[new_row][new_col] == float("inf")
                ):
                    # The max value encountered on the path to this cell.
                    min_value_to_reach[new_row][new_col] = max(
                        current[0], grid[new_row][new_col]
                    )

                    # Add the cell to the heap for further exploration.
                    min_heap.put(
                        (min_value_to_reach[new_row][new_col], new_row, new_col)
                    )

        # Use binary search to determine the maximum number of points that can
        # be collected for each query.
        for i in range(query_count):
            threshold = queries[i]
            left, right = 0, total_cells

            # Find the rightmost number of points we can collect before
            # exceeding the query threshold.
            while left < right:
                mid = left + (right - left + 1) // 2

                if threshold_for_max_points[mid] < threshold:
                    left = mid
                else:
                    right = mid - 1

            # Return `left`.
            result[i] = left

        return result
    

