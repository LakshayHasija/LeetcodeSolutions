class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        res = [0] * numberOfUsers
        online = [(1,-1) for _ in range(numberOfUsers)] 
        for e in events:
            timestamp = int(e[1])
            for i in range(len(online)):
                status, time = online[i]
                if status == 0 and time + 60 <= timestamp:
                    online[i] = (1, -1)
            if e[0] == "OFFLINE":
                userId = int(e[2])
                online[userId] = (0, timestamp)
                print('offline', online)
            elif e[0] == "MESSAGE":
                mentions = e[2]
                if mentions == "HERE":
                    for i in range (len(online)):
                        if online[i][0] == 1:
                            res[i] += 1
                    print('here message', res)                        
                elif mentions == "ALL":
                    for i in range(len(res)):
                        res[i] +=1
                else:
                    temp = mentions.split()
                    idxs = [int(x[2:]) for x in temp]
                    for idx in idxs:
                        res[idx] +=1
                    print('message', res)
        return res