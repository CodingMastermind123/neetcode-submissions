class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightprod = 1
        leftprod = 1
        newList = []
        i = 0
        j = 1
        index = 0
        for num in nums:
            i = 0
            j = index + 1
            rightprod = 1
            leftprod = 1
            while i < index:
                leftprod *= nums[i]
                i += 1
            while j < len(nums):
                rightprod *= nums[j]
                j += 1
            newList.append(leftprod * rightprod)
            index += 1
        
        return newList

            

                

       