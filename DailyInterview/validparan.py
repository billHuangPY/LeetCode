class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pop_char = {')':'(','}':'{',']':'['}
        for c in s:
            if c in pop_char:
                if len(stack) < 1 or not stack[-1] == pop_char[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
                
        if len(stack) == 0:
            return True
        return False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

