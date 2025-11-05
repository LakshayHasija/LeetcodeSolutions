from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = [0] * (n - k + 1)
        freq = defaultdict(int)
        def cmp_key(v):
            return (freq[v], v)
        topX = SortedList(key=cmp_key)
        rest = SortedList(key=cmp_key)
        sumTop = 0
        def rebalance():
            nonlocal sumTop
            while len(topX) < x and len(rest) > 0:
                best = rest[-1]
                rest.remove(best)
                topX.add(best)
                sumTop += freq[best] * best
            while len(topX) > x:
                worst = topX[0]
                topX.remove(worst)
                rest.add(worst)
                sumTop -= freq[worst] * worst
            while topX and rest:
                worstTop = topX[0]
                bestRest = rest[-1]
                fw, fr = freq[worstTop], freq[bestRest]
                if fr > fw or (fr == fw and bestRest > worstTop):
                    topX.remove(worstTop)
                    rest.remove(bestRest)
                    topX.add(bestRest)
                    rest.add(worstTop)
                    sumTop += fr * bestRest - fw * worstTop
                else:
                    break
        for i in range(n):
            v = nums[i]
            old = freq[v]
            if old > 0:
                if v in topX:
                    topX.remove(v)
                    sumTop -= old * v
                elif v in rest:
                    rest.remove(v)
            freq[v] = old + 1
            rest.add(v)
            rebalance()
            if i >= k:
                u = nums[i - k]
                oldU = freq[u]
                if u in topX:
                    topX.remove(u)
                    sumTop -= oldU * u
                elif u in rest:
                    rest.remove(u)
                if oldU == 1:
                    del freq[u]
                else:
                    freq[u] = oldU - 1
                    rest.add(u)
                rebalance()
            if i >= k - 1:
                ans[i - k + 1] = sumTop
        return ans