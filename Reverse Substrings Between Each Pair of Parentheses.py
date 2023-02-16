class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            ind = 0
            for i in range(len(s)):
                if s[i] == '(':
                    ind = i
                elif s[i] == ')':
                    s = s.replace(s[ind : i + 1], s[ind + 1 : i][::-1])
                    break 
        return s
