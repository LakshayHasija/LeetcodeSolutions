class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        is_prime=[True]*n
        is_prime[0]=is_prime[1]=False
        for i in range(2,int(n**0.5)+1): #sqrt n + 1
            if is_prime[i]:
                for j in range(i**2,n,i): #mark its multiples as False
                    is_prime[j]=False
        return sum(is_prime)