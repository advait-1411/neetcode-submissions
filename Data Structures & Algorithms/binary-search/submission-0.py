class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0 , len(nums)-1

        while l<=h:
            m = l + (h-l)//2

            if nums[m]== target:
                return m
            
            if target > nums[m]:
                l = m + 1
            
            if target < nums[m]:
                h = m -1
            
        return -1