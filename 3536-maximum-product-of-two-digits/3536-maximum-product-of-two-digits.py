class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]
        for i in (str(n)):
            arr.append(int(i))
        a=max(arr)
        arr.remove(a)
        b=max(arr)
        return a*b    
        