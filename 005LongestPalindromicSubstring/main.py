class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_list = []

        for idx_item, item in enumerate(s):
            if item in temp_list:
                idx_first = temp_list.index(item)


        if max == 0:
            return ""

        return

if __name__ == "__main__":
    num = 'abc'
    s = Solution()
    print s.longestPalindrome(num)