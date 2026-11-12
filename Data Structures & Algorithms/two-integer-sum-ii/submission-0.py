class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        st = 0
        end = n-1
        while st<end:
            if numbers[st]+numbers[end] == target:
                return [st+1,end+1]
            # num[st] is likely short 
            elif numbers[st] + numbers[end] < target:   
                st += 1
            elif numbers[st] + numbers[end] > target:
                end -=1
        return 