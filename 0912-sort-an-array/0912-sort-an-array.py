class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums,beg,end):
            if beg<end:
                mid=(beg+end)//2
                merge_sort(nums,beg,mid)
                merge_sort(nums,mid+1,end)
                merge(nums,beg,mid,end)
        def merge(nums,beg,mid,end):
            i=beg
            j=mid+1
            temp=[]
            while i<=mid and j<=end:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i=i+1
                else:
                    temp.append(nums[j])
                    j=j+1
            if i>mid:
                while j<=end:
                    temp.append(nums[j])
                    j=j+1
            else:
                while i<=mid:
                    temp.append(nums[i])
                    i+=1
            for k in range (len(temp)):
                nums[beg+k]=temp[k]
        merge_sort(nums,0,len(nums)-1)  
        return nums                                        

        