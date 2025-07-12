class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        lst = set("aeiouAEIOU")
        while left <= right:
            if not s[left] in lst:
                left += 1
            elif not s[right] in lst:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)