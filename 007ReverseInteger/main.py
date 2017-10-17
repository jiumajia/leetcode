class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 1
        if x < 0:
            x = abs(x)
            flag = -1
        res = flag*int((str(x)[::-1]))
        if abs(res) > 2147483647:
            return 0
        return res

if __name__ == "__main__":
    num = -123
    s = Solution()
    print s.reverse(num)