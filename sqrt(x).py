class Solution:
    def mySqrt(self, x: int) -> int:
     if x < 2:
      return x
     L=1
     R=x
     while L < R:
      mid = (L+R)//2
      if mid*mid == x:
       return mid
      if mid*mid > x:
       R = mid
      if mid*mid < x:
       L = mid+1
       mid = (L+R)//2
       if mid*mid == x:
        return mid
       elif mid*mid > x:
        return L-1