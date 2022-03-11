from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target > nums[i]:
                continue
            return i
        return len(nums)