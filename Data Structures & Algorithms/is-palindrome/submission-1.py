class Solution:
    def isPalindrome(self, string: str) -> bool:
        cleaned_string  = [] # O(n)
        rev_string = [] # O(n)
        for c in string: # O(n)
            if c.isalnum(): 
                cleaned_string.append(c.lower())
                rev_string.append(c.lower())

        return cleaned_string[:] == rev_string[len(rev_string)-1::-1] #O(n) 

#O(n),O(n)