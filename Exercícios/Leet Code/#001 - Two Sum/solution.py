class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        for idx1 in range(0, len(nums)):
            soma = 0
            for idx2 in range(idx1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    return [nums[idx1], nums[idx2]]



    twoSum("x", [2,7,11,15], 9)