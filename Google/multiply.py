'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''
## Time: O(M*N) Space: O(M+N)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        ans = [0]*(len(num1)+len(num2))
        for i1, n1 in enumerate(num1[::-1]):
            for i2, n2 in enumerate(num2[::-1]):
                
                pos = i1 + i2
                val = ans[pos] + int(n1)*int(n2)
                ans[pos + 1] += int(val / 10)
                ans[pos] = val % 10
                ## print(i1, i2, n1, n2, val, ans)
                
        while ans[-1] == 0:
            ans.pop()
            
        return "".join([str(i) for i in ans[::-1]])