class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_string = list(s)

        temp_list = []

        max = 0
        for item in list_string:

            if item in temp_list:

                idx = temp_list.index(item)

                temp_list = temp_list[idx+1:]

            temp_list.append(item)

            if max < len(temp_list):
                max = len(temp_list)

        return max


if __name__ == "__main__":
    num = "pwwkew"
    s = Solution()
    print s.lengthOfLongestSubstring(num)