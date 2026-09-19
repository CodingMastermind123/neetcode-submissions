class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        list2 = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            list2.append((nums[i], j - i))
            i = j
            
            
        list2.sort(key = lambda x:x[1], reverse = True)
        return [list2[x][0] for x in range(k)]
