from typing import List


class Solution:
    """
    Find the common prefix
    """
    @staticmethod
    def longest_commonPrefix(strings: List[str]) -> str:
        """
        Find the common prefix by utilizing horizontal scanning.

        :param strings: list of strings
        :return:        longest common prefix.
        """

        # By default, we store entire first string as a prefix.
        prefix = strings[0]

        # iterate over all the stings, except the first one.
        for s in strings[1:]:
            # Then iterate over all symbols of the current string.
            for i in range(len(prefix)):
                # Check if the string starts with a prefix
                if s.startswith(prefix):
                    # if so, we are done with that string,
                    break
                else:
                    # if not, we shorten the string by one.
                    prefix = prefix[:-1]

        return prefix
