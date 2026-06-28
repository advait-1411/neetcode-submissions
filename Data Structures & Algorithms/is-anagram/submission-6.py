class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {c:0 for c in s}
        for c in s:
	        s_hash[c] += 1

        t_hash = {c:0 for c in t}
        for c in t:
   	    	t_hash[c] += 1
        
        for (k,v) in s_hash.items():
            if (k,v) not in t_hash.items():
                return False 
                    
        return True