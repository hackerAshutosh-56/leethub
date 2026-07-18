class Solution:
    def findGCD(self, nums):
        def gcd(a,b):
            if (b%a==0):
                return a
            else:
                return gcd(b%a,a)
        a=min(nums)
        b=max(nums)
        return  gcd(a,b)
