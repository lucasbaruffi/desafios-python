class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    
        for i in range(0, len(nums)):
            if target - nums[i] in nums:
                if nums.index(target - nums[i]) != i:
                    return [i, nums.index(target - nums[i])] 


    print(twoSum("x", [2,7,11,15], 9))