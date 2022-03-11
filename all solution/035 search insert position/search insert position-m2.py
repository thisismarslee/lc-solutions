from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target > nums[i]:
                if i == len(nums)-1:
                    return len(nums)
                continue
            return i