from typing import List


class Solution:
    """
    The solution is based on using a hash map (python dictionary)
    It's a trade off between speed and memory usage
    As we store every possible answer in the hash map
    """
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """
        Solution

        :param nums:    list of numbers to check
        :param target:  target sum
        :return:        list of the addend indexes
        """
        # stores all possible values
        hash_map = {}
        # we cant determine an answer unless iterating over the list
        for index, n in enumerate(nums):
            # if the hash map does not contain the value we store
            # we store the target - n as a key key and index as a value

            # its important to check None explicitly, as we can have 0
            if hash_map.get(n) is not None:
                if hash_map[n] != index:
                    return [hash_map[n], index]
            hash_map[target - n] = index

        return []
