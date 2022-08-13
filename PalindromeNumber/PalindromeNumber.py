import math


class Solution:
    def isPalindromeString(self, x: int) -> bool:
        stringX = str(x)
        for i in range(len(str(stringX))):
            if stringX[i] != stringX[-i - 1]:
                return False
        return True

    def isPalindromeList(self, x: int) -> bool:
        step = 10
        i = 1
        toDivide = True
        nums = []
        while toDivide:
            a = x // i % step
            if a:
                nums.append(a)
                i *= step
            else:
                toDivide = False

        for i in range(len(nums)):
            if nums[i] != nums[-i - 1]:
                return False
        return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numberLength = math.ceil(math.log10(x + 1))
        step = 10
        for i in range(math.ceil(numberLength / 2)):
            if x // pow(step, i) % step != x // pow(step, numberLength - i - 1) % step:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(122))
