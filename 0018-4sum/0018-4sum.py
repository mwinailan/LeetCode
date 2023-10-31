class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        currKSums = []
        # generalized approach to calculating sums > 2
        def kSum(k, start, target):
            # Case 1: If k is not 2, recursively find elements that sum up to the target
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    currKSums.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    currKSums.pop()
                return
            
            # Case 2: If k is 2, conduct a two pointer solution to find the target
            # Calculate whether the values at left and right pointers sum to the the target
            left, right = start, len(nums) - 1
            while(left < right):
            # Case 2.1 : If sum is larger than target, then we find a smaller sum of nums[left] and nums[right]
                if nums[left] + nums[right] > target:
                    right -= 1
            # Case 2.2 : If sum is smaller than target, then we find a larger sum of nums[left] and nums[right]
                elif nums[left] + nums[right] < target:
                    left += 1
            # Case 2.3: If sum is equal to the target, then we append nums[left] and nums[right] to currKSums and to the res list
                else:
                    res.append(currKSums + [nums[left], nums[right]])
                    left += 1
                    # Account for potential value duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        kSum(4, 0, target)
        return res