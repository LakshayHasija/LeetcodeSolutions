class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers=0
        current_row=[0,0]
        for i in range(len(bank)):
            if "1" in bank[i]:
                if current_row[0]==i:
                    current_row[1]=bank[i].count("1")
                    continue
                else:
                    temp=bank[i].count("1")
                    lasers+=current_row[1]*temp
                    current_row=[i,temp]
        return lasers
