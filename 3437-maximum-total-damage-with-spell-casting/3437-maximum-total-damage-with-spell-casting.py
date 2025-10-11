class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq=Counter(power)
        power_cnt=[]
        for p in sorted(freq.keys()):
            power_cnt.append((p,freq[p]))
        cache = {}
        
        def binarySearchNextIndex(targetPower):
            l,r=0,len(power_cnt)
            while l<r:
                m=(l+r)//2
                if power_cnt[m][0]<targetPower:
                    l=m+1
                else:
                    r=m
            return l

        def getMaxDamage(index):
            if index in cache:
                return cache[index]
            if index >= len(power_cnt):
                return 0
            notDamage = getMaxDamage(index + 1)
            curPower, curCnt = power_cnt[index]
            nxtIndex = binarySearchNextIndex(curPower + 3)
            damage = curPower * curCnt + getMaxDamage(nxtIndex)
            cache[index] = max(notDamage, damage)
            return cache[index]

        return getMaxDamage(0)
