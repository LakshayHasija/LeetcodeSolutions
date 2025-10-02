class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk=0
        filled=numBottles
        unfilled=0
        while filled>0:
            drunk+=filled
            unfilled+=filled
            filled=0
            if unfilled>=numExchange:
                filled=1
                unfilled-=numExchange
            numExchange+=1
        return drunk