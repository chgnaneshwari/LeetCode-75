import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Find the greatest common divisor of the lengths of str1 and str2
        gcd_len = math.gcd(len(str1), len(str2))
        
        # Step 2: Candidate string is the first part of str1 with length gcd_len
        candidate = str1[:gcd_len]
        
        # Step 3: Check if this candidate divides both str1 and str2
        if str1 == candidate * (len(str1) // gcd_len) and str2 == candidate * (len(str2) // gcd_len):
            return candidate
        else:
            return ""  # No common divisor string
