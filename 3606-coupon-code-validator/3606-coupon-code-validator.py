import re
class Solution:
    def valid_code(self,s):
        return bool(re.fullmatch(r'[A-Za-z0-9_]+', s))
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans=[]
        valid_line=["electronics", "grocery", "pharmacy", "restaurant"]
        electronics=[]
        grocery=[]
        pharmacy=[]
        restaurant=[]
        for i in range(len(code)):
            if self.valid_code(code[i]) and (businessLine[i] in valid_line) and isActive[i]:
                if businessLine[i]=="electronics":
                    electronics.append(code[i])
                elif businessLine[i]=="grocery":
                    grocery.append(code[i])
                elif businessLine[i]=="pharmacy":
                    pharmacy.append(code[i])
                else:
                    restaurant.append(code[i])
        electronics.sort()
        grocery.sort()
        pharmacy.sort()
        restaurant.sort()
        ans.extend(electronics+grocery+pharmacy+restaurant)
        return ans