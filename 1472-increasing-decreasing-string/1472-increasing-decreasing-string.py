class Solution:
    def sortString(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        while len(result) < len(s):
            # Increasing pass
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
            # Decreasing pass
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1

        return ''.join(result)
