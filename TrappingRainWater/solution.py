from typing import List


class Solution:
    """
    To compute the container with the most water
    Both recursive and two-way scanning can be used
    """

    @staticmethod
    def find_2_maxes(height_list: List[int]) -> \
            ((int, int), (int, int)):
        """
        From a given list finds two maximum values.

        :param height_list:     list of heights to find two maximums
        :return:                two tuples of integers: first is the index; the second is the value
        """

        # The tuples store the index and the value
        # By default, the first values the first element
        # The second are the minimum
        max_first = 0, height_list[0]
        max_second = 0, 0

        # Cycle the elements in the list
        for i, value in enumerate(height_list):
            # the change of the second maximum depends on two conditions:
            #   it is bigger than the previous value
            #   it is further away from the beginning

            # if the value is bigger than the second maximum
            # it is swapped with the first and updated
            if value >= max_first[1] and i != max_first[0]:
                max_second = max_first
                max_first = i, value
            elif value >= max_second[1] and i != max_second[0]:
                max_second = i, value

        return max_second, max_first

    @staticmethod
    def trap_recursively(height_list: List[int]) -> int:
        """
        Recursive implementation
        Splits the heights list and recursively finds its values
        :param height_list:
        :return:
        """
        # if the list is 2 values long
        # it cannot hold any water
        if len(height_list) <= 2:
            return 0
        # accumulates the total collected water
        total = 0
        # finds the first and second maximums of the heights list
        first, second = Solution.find_2_maxes(height_list)

        # indexes of the maximums
        # sorted to preserve right sides
        bounds = sorted([first[0], second[0]])

        # the upper bound that can hold the water
        bound = min(first[1], second[1])

        # the part of the heights list that holds the water by the bound
        bounded = height_list[bounds[0]:bounds[1] + 1]
        # we don't compute values at the maximums as they are always 0
        for i in bounded[1:-1]:
            # we add the delta to the total
            total += bound - i

        # we split the list in left and right parts
        left = height_list[0:bounds[0] + 1]
        right = height_list[bounds[1]:]

        # we call the method recursively for the left and right sides
        # adding its result to the total
        return total + Solution.trap_recursively(right) + Solution.trap_recursively(left)

    @staticmethod
    def trap_scanning(height_list: List[int]) -> int:
        """
        To avoid recursive calls
        we can implement the solution by scanning the list
        and counting the total water
        :param height_list:
        :return:
        """

        # the left and right scan indexes
        left = 0
        right = len(height_list) - 1

        # and their corresponding values
        l_max = height_list[left]
        r_max = height_list[right]

        # accumulates the total collected water
        total = 0

        # we scan the list until right and left collide
        while left != right:
            # the upper bound that can hold the water
            bound = min(l_max, r_max)

            # we scan from right to left if left is bigger
            # and vise versa
            if l_max > r_max:
                right -= 1

                # if the current value is bigger
                # we update the maximum
                if height_list[right] >= r_max:
                    r_max = height_list[right]
                # we add the delta to the total
                else:
                    total += bound - height_list[right]
            # the same proces only for the other side
            else:
                left += 1
                if height_list[left] >= l_max:
                    l_max = height_list[left]
                else:
                    total += bound - height_list[left]

        return total
