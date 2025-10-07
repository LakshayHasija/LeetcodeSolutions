class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake_rain_days = defaultdict(list)
        for day,lake in enumerate(rains):
            if lake>0:
                lake_rain_days[lake].append(day)
        result=[-1]*len(rains)
        full_lakes=set()
        dry_days=[]
        lake_to_next_rain={}
        import heapq
        next_rains=[]
        for i,lake in enumerate(rains):
            if lake>0:
                if lake in full_lakes:
                    return []
                full_lakes.add(lake)
                lake_rain_days[lake].pop(0)  #remove today
                if lake_rain_days[lake]:
                    heapq.heappush(next_rains,(lake_rain_days[lake][0],lake))
                result[i]=-1
            else:
                if next_rains:
                    next_day,lake_to_dry=heapq.heappop(next_rains)
                    result[i]=lake_to_dry
                    full_lakes.remove(lake_to_dry)
                else:
                    result[i]=1
        return result