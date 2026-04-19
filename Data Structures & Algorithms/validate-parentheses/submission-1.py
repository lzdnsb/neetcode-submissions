class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if s[i] in '([{':
                stack.append(s[i])
            elif s[i] in ')]}':
                if s[i] == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if s[i] == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if s[i] == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            i += 1

        if len(stack) == 0:
            return True
        return False

