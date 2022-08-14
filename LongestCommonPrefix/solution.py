from typing import List


class Solution:
    """
    To find the common prefix
    We use horizontal scanning
    """
    @staticmethod
    def longest_commonPrefix(strings: List[str]) -> str:
        """
        Solution

        :param strings: list of strings
        :return:        longest common prefix
        """

        # by default we store entire first string as a prefix
        prefix = strings[0]

        # than we iterate over all of the stings, except the first one
        for s in strings[1:]:
            # then we iterate over all symbols of the current string
            for i in range(len(prefix)):
                # we check, if the string starts with a prefix
                if s.startswith(prefix):
                    # if so, we are done with that string
                    break
                else:
                    # if not, we shorten the string by one
                    prefix = prefix[:-1]

        return prefix
