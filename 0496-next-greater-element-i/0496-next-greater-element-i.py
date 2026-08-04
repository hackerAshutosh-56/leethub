class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans=[]
        n= len(nums2)
        for i in range (n-1,-1,-1):
            while (len(stack)!=0 and stack[-1]<nums2[i]):
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(nums2[i])    
        ans.reverse()
        result=[]
        for i in nums1:
            a=nums2.index(i)
            result.append(ans[a])
        return result                    