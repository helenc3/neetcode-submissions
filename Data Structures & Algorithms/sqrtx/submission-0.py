class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        i = 0
        while(lo <= hi):
            mid = lo + (hi-lo)//2
            if (mid * mid > x):
                hi = mid-1
            elif (mid * mid < x):
                lo = mid + 1
            else:
                return mid
        return hi



        