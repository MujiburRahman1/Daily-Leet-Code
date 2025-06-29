class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenght = 0
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            i -= 1
            lenght += 1
        return lenght