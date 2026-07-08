class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {x:0 for x in nums}     
        for n in nums:
          hash[n] += 1
          if hash[n] >1:
               return True
        return False