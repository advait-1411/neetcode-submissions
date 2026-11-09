class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    # Shortest string
        prefix = min(strs,key=len)    #O(n)
        
        for s in strs: #O(n)
            i=0
            while i<len(prefix) and prefix[i]==s[i]: #O(k where k = len(prefix))
                i+=1
            prefix=prefix[:i]
        return prefix