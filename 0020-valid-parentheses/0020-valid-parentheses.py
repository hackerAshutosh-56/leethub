class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in["(", "{", "["]:
                stack.append(i)
            if i==")":
                if len(stack)==0 or stack[-1]!="(" :
                    return False
                stack.pop()   
            if i=="}":
                if len(stack)==0 or stack[-1]!="{" :
                    return False
                stack.pop()  
            if i=="]":
                if len(stack)==0 or stack[-1]!="[" :
                    return False
                stack.pop()     
        if len(stack)==0:
            return True
        else:
            return False    