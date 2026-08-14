class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        path=[]
        def backtrack(start):
            if start==len(s):
                ans.append(path[:])
                return 
            for i in range(start,len(s)):
                ss=s[start:i+1]
                if ss==ss[::-1]:
                    path.append(ss)
                    backtrack(i+1)
                    path.pop()
        backtrack(0) 
        return ans               
        