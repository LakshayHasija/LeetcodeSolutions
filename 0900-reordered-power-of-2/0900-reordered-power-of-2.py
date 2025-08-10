class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(num):
            return ''.join(sorted(str(num)))
        count=count_digits(n)
        for i in range(31):
            p2=2**i
            if count_digits(p2)==count:
                return True
        return False
