class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [num for row in grid for num in row]
        arr.sort()
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1
        median = arr[len(arr) // 2]
        operations = 0
        for num in arr:
            operations += abs(num - median) // x
        return operations