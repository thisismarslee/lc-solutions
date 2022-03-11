from typing import List


class Solution(object):
    """
    this is a class for leedcode solution
    """

    @staticmethod
    def f001(nums: List[int], target: int) -> List[int]:
        # 001 method 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return -1

    @staticmethod
    def f001_2(nums: List[int], target: int) -> List[int]:
        # 001 method2
        nums_index = 1
        for num in nums:
            num_tofind = target - num
            if num_tofind in nums[nums_index:]:
                return [nums.index(num, 0), nums.index(num_tofind, nums_index)]
            nums_index += 1
        return -1

    @staticmethod
    def f035(nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target > nums[i]:
                continue
            return i
        return len(nums)

    @staticmethod
    def f035_2(nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target > nums[i]:
                if i == len(nums)-1:
                    return len(nums)
                continue
            return i
