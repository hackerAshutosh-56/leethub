class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(path):
            if(len(path)==len(nums)):
                ans.append(path[:])
                return 

            for i in nums:
                if i not in path:
                    path.append(i)
                    solve(path)
                    path.pop()
        solve([])
        return ans            