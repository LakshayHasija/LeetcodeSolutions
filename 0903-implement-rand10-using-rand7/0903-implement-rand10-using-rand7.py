# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        ans=0
        for _ in range(10):
            ans+=rand7()    #[1,7]*10-->[10,70]
        return (ans%10)+1   #[0,9]+1-->[1,10]