class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i, j = 0, 0
        
        # Loop through both strings
        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1
            j += 1
        
        # Add remaining characters from word1
        result += word1[i:]
        
        # Add remaining characters from word2
        result += word2[j:]
        
        return result
