class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0],reverse=True)
        req_energy=0
        energy_left=0
        for actual,minimum in tasks:
            if energy_left<minimum:
                extra=minimum-energy_left
                req_energy+=extra
                energy_left+=extra
            energy_left-=actual
        return req_energy