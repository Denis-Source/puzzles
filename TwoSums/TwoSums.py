from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for index, n in enumerate(nums):
            if hMap.get(n, None) is not None:
                if hMap[n] != index:
                    return [hMap[n], index]
            hMap[target - n] = index

        return []


if __name__ == '__main__':
    print(Solution().twoSum([7, 4, 2, 1, 3, 5, 4], 10))
