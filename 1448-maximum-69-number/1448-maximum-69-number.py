class Solution:
    def maximum69Number (self, num: int) -> int:
        strnum=str(num)
        for i in range(len(strnum)):
            if strnum[i]=="6":
                strnum=strnum[0:i]+"9"+strnum[i+1:]
                break
        return int(strnum)