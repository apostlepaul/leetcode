class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sum = sum(nums)
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            half = (nums_sum + nums[i])/2
            if cum_sum == half:
                return i
        else:
            return -1
