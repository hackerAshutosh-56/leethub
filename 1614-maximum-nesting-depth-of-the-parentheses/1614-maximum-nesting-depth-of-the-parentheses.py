class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        ans=0
        result=0
        for i in s:
            if i=="(":
                ans+=1
                result=max(ans,result)
            if i==")":
                ans=ans-1
        return result  
        