class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        result = []
        i = j = 0 
        while i < n or j < m:
            if i < n:
                result.append(word1[i])
                i += 1
            if j < m:
                result.append(word2[j])
                j += 1
        return "".join(result)