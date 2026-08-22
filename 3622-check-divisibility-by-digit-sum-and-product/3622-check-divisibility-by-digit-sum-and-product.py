class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumOfDigits=0
        productOfDigits=1
        num=n
        while num>1:
            temp=num%10
            sumOfDigits+=temp
            productOfDigits*=temp
            num//=10
        if num==1:
            sumOfDigits+=1
        print(n,sumOfDigits,productOfDigits)
        return n%(sumOfDigits+productOfDigits)==0