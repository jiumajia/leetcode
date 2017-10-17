class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 1
        if x < 0:
            return False
        res = flag*int((str(x)[::-1]))
        if res > 2147483647:
            return False
        if res == x:
            return True
        else:
            return False

if __name__ == "__main__":
    num = 121
    s = Solution()
    print s.isPalindrome(num)