class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        used=[False]*len(nums)
        def solve(arr):
            if len(arr)==len(nums):
                ans.append(arr[:])
                return
            for i in range (len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue

                arr.append(nums[i])            
                used[i]=True
                solve(arr)

                arr.pop()
                used[i]=False
        solve([])
        return ans        