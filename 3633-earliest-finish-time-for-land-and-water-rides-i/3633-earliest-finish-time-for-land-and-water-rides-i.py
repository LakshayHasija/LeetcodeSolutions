class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        landEndTime=[]
        waterEndTime=[]
        for i in range(len(landStartTime)):
            landEndTime.append(landStartTime[i]+landDuration[i])
        for i in range(len(waterStartTime)):
            waterEndTime.append(waterStartTime[i]+waterDuration[i])
        land_finish=min(landEndTime)
        opt1 = min(max(land_finish, waterStartTime[i]) + waterDuration[i] for i in range(len(waterStartTime)))
        water_finish=min(waterEndTime)
        opt2=min(max(water_finish,landStartTime[i])+landDuration[i] for i in range(len(landStartTime)))
        return min(opt1, opt2)