from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_index = 1
    for num in nums:
        num_tofind = target - num
        if num_tofind in nums[nums_index:]:
            return [nums.index(num, 0), nums.index(num_tofind, nums_index)]
        nums_index += 1
    return -1
