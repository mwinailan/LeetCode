class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        nums.sort()
        answers = []
        
        for i in range(len(nums)):
            if (i > 0 and nums[i-1] == nums[i]):
                continue
            left = i + 1
            right = len(nums) -  1

            while ( left < right ):
                total = nums[i] + nums[left] + nums[right]
                if (total < 0):
                    left = left + 1
                elif (total > 0):
                    right = right - 1
                else:
                    answers.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    while (left < right and nums[left] == nums[left-1]):
                        left = left + 1
        return answers

        