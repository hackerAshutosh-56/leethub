class Solution:
    def check(self, nums: List[int]) -> bool:
        k=0
        n=len(nums)
        for i in range (n-1):
            if nums[i]>nums[i+1]:
                k=k+1
        if nums[-1]>nums[0]:
            k+=1
        if k<=1:
            return True
        else:
            return False        
        