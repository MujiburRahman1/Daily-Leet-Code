class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if string 't' is an anagram of string 's'.

        Args:
          s: The first string.
          t: The second string.

        Returns:
          True if 't' is an anagram of 's', False otherwise.
        """

        # Agar dono strings ki length same nahi hai, to False return karen
        if len(s) != len(t):  # Check if the lengths of the strings are different
            return False  # If lengths are different, they can't be anagrams

        # Dictionaries banayen har string ke characters ki frequency              count karne ke liye 
        countS = {}  # Initialize an empty dictionary to count characters in 's'
        countT = {}  # Initialize an empty dictionary to count characters in 't'

        # Har string ke characters ki frequency count karen
        for i in range(len(s)):  # Iterate through each character in 's' using its index
            countS[s[i]] = 1 + countS.get(s[i], 0)  # Increment the count of s[i] in countS
            countT[t[i]] = 1 + countT.get(t[i], 0)  # Increment the count of t[i] in countT

        # Agar dono dictionaries same hain, to True return karen
        return countS == countT  # Check if both dictionaries have the same key-value pairs