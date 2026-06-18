class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #360 min hand - 30 hour hand moves
        #1 min hand move - 1/12 hour hand moves
        #1 min 6 degree
        minhandangle=6*minutes
        hourhandangle=(hour*30+(minutes/2))%360
        # print(minhandangle,hourhandangle)
        angle=abs(minhandangle-hourhandangle)
        return angle if angle<=180 else 360-angle