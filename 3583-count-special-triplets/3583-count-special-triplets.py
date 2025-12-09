class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        cnt = defaultdict(int)
        pair = defaultdict(int)
        res = 0
        for n in nums:
            if n in cnt:
                res += pair[n] % MOD
            if n * 2 in cnt:
                pair[n * 2] += cnt[n * 2] % MOD
            cnt[n] += 1
        return res % MOD