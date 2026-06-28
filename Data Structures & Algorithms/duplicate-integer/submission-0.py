class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {i:0 for i in nums}
        for i in nums:
            hash[i] += 1
            if hash[i] >1:
                return True
        return False