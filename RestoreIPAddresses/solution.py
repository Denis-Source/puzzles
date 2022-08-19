import re
from typing import List


class Solution:
    DOT = "1"
    VALID_IP_RE = re.compile(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$")

    def restoreIpAddresses(self, s: str) -> List[str]:
        addresses = []
        if 4 <= len(s) <= 16:
            for i in range(pow(2, len(s))):
                potential_addr = ""
                dots_location = f"{i:0{len(s)}b}"
                for index, dot in enumerate(dots_location):
                    potential_addr += s[index]
                    if dot == self.DOT:
                        potential_addr += "."
                if self.VALID_IP_RE.match(potential_addr):
                    addresses.append(potential_addr)

            return addresses
        else:
            return []


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("2" * 12))
