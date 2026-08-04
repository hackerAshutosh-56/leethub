class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        m=[]
        for i in range (a,b):
            if (i not in nums):
                m.append(i)
        return m        
        