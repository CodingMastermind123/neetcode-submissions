class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answerList = []

        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                numSum = nums[i] + nums[left] + nums[right]
                if numSum == 0:
                    answerList.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif numSum < 0:
                    left += 1
                else:
                    right -= 1
        
        return answerList

                



        