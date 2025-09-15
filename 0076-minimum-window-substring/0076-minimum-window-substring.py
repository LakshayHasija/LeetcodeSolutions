class Solution:
    def check(self,t_count,s_count):
        for key,value in t_count.items():
            if t_count[key]>s_count[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count=Counter(t)
        s_count=defaultdict(int)
        i=0  # Left pointer
        min_len=float("inf")
        res=""
        for j in range(len(s)):  # Right pointer
            s_count[s[j]]+=1
            while self.check(t_count,s_count):
                if (j-i+1)<min_len:
                    min_len=j-i+1
                    res=s[i:j+1]
                s_count[s[i]]-=1
                i+=1
        return res