class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for x in nums1:
            idx=nums2.index(x)
            greater=-1
            for i in range (idx+1,len(nums2)):
                if nums2[i]>x:
                    greater=nums2[i]
                    break
            ans.append(greater)
        return ans            
        