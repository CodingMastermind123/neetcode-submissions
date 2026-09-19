class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        i = 0
        while i < len(nums):
            for j in range(0, len(nums)):
                if j != i:
                    if nums[j] + nums[i] == target:
                        sol = [j, i]
            i += 1
        return sol