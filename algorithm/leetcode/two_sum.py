"""
This is TwoSum class module
"""


class TwoSum(object):
    """
    This is TwoSum class
    """

    def two_sum(self, nums, target):
        """
        two sum solution

        Args:
            nums: [int]
            target: int
        Returns:
            res: [int, int]
        Raises:
            None
        """
        dic = {}
        for i, val in enumerate(nums):
            if target - val in dic:
                return [dic.get(target - val), i]
            dic[val] = i
        return None
