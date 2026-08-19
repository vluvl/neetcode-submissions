class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openP = ['(','[','{']
        closeP = [')',']','}']
        for c in s:
            if c in openP:
                stack.append(openP.index(c))
            elif c in closeP and stack and stack[-1] == closeP.index(c):
                stack.pop()
            else:
                return False
        if not stack: 
            return True
        else:
            return False