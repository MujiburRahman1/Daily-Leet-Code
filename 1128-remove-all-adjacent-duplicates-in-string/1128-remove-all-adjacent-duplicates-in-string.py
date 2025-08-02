class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            # Remove the last character from the stack if it's the same as the current one
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
                
        return ''.join(stack)