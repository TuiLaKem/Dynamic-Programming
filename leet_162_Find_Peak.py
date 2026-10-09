class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        peak = 0
        for i in range (len(nums)):
            if nums[i] > nums[peak]:
                peak = i

        return peak
