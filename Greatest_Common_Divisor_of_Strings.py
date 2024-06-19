class Solution(object):
    def gcd(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        gcd_len = self.gcd(len1, len2)

        candidate = str1[:gcd_len]

        if candidate * (len1 // gcd_len) == str1 and candidate * (len2 // gcd_len) == str2:
            return candidate
        else:
            return ""


# Example usage:
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))  # Output: ""
