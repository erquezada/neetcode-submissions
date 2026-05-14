class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 # right pointer
        right = len(s) - 1 # left pointer

        while left < right: # iterate through string
            # Step 1: skip non-alphanumeric on left
            if not s[left].isalnum():
                left += 1
                continue
            # Step 2: skip non-alphanumeric on right
            if not s[right].isalnum():
                right -= 1
                continue
            # Step 3: compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            # Step 4: move pointers
            left += 1
            right -= 1
        return True