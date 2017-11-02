class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 1:
            return s
        if size == 2:
            if s[0] == s[1]:
                return s
            return s[0]
        maxp = 1
        ans = s[0]
        i = 0
        while i < size:
            j = i + 1
            while j < size:
                if s[i] == s[j]:
                    j += 1
                else:
                    break
            k = 0
            while i - k - 1 >= 0 and j + k<= size - 1:
                if s[i- k - 1] != s[j + k]:
                    break
                k += 1
            if j - i + 2*k > maxp:
                maxp = j- i + 2*k
                ans = s[i - k:j + k]
            if j + k == size - 1:
                break
            i = j
        return ans

    def longestPalindrome_test(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_list = []

        longest_count = 0
        longest_str = ""
        for idx_item, item in enumerate(s):
            for x in range(0, len(s[idx_item+1:])+1):
                end_idx = idx_item+x+1
                if s[idx_item:end_idx] == s[idx_item:end_idx][::-1]:
                    if longest_count < len(s[idx_item:end_idx]):
                        longest_str = s[idx_item:end_idx]
                        longest_count = len(s[idx_item:end_idx])
            if longest_count >= len(s[idx_item:]):
                break

        return longest_str



if __name__ == "__main__":
    num = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
    s = Solution()
    print(s.longestPalindrome(num))
    print(s.longestPalindrome_test(num))