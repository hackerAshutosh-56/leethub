class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def solve(start,target,path):
            
            if target==0:
                ans.append(path[:])
                return 
            if target<0:
                return
            for i in range (start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                solve(i+1,target-candidates[i],path)
                path.pop()
        solve(0,target,[])
        return ans        
        