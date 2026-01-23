class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        heap, cnt_decrease, steps, n = [], 0, 0, len(nums)
        for i, (a, b) in enumerate(pairwise(nums)):
            heappush(heap, (a+b, i))
            cnt_decrease += (a > b)

        prev, next = [*range(-1, n-1)], [*range(1, n+1)]
        next[-1] = -1
        while cnt_decrease:
            s, a = heappop(heap)
            b = next[a]
            if s == nums[a] + nums[b]:
                cnt_decrease -= (nums[a] > nums[b])
                if prev[a] != -1:
                    heappush(heap, (s + nums[prev[a]], prev[a]))
                    cnt_decrease += (nums[prev[a]] > s) - (nums[prev[a]] > nums[a])
                if next[b] != -1:
                    heappush(heap, (s + nums[next[b]], a))
                    cnt_decrease += (s > nums[next[b]]) - (nums[b] > nums[next[b]])
                nums[a], nums[b] = s, inf
                next[a], prev[next[b]] = next[b], a
                steps += 1
        return steps