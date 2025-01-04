class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Step 1: Remove unwanted characters (non-alphanumeric)
    # and convert to lowercase
     filtered_str = ''.join(c.lower() for c in s if c.isalnum())
    
    # Step 2: Use two pointers to compare characters from both ends
     left, right = 0, len(filtered_str) - 1
    
     while left < right:
        if filtered_str[left] != filtered_str[right]:
            return False
        left += 1
        right -= 1
    
     return True
