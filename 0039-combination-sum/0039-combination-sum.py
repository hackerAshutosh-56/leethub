class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        def solve (start,target,path):
            if target==0:
                ans.append(path[:])
                return
            if target<0:
                return
            for i in range (start,len(candidates)):
                path.append(candidates[i])
                solve(i,target-candidates[i],path) 
                path.pop()
        solve(0,target,[])
        return ans           