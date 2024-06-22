# Given 3 positives numbers a, b and c. Return the minimum flips required in some
# bits of a and b to make ( a OR b == c ). (bitwise OR operation). Flip operation
# consists of change any single bit 1 to 0 or change the bit 0 to 1 in their
# binary representation.
# 0010 -> a
# 0110 -> b
# 0101 -> c
# 0001 -> a
# 0100 -> b
# 0101 -> c
#
# Example
# 1:
#
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After
# flips
# a = 1, b = 4, c = 5
# such that(a OR b == c)
# Example 2:
#
# Input: a = 4, b = 2, c = 7
# Output: 1
# Example 3:
#
# Input: a = 1, b = 2, c = 3
# Output: 0
#
# Constraints:
#
# 1 <= a <= 10 ^ 9
# 1 <= b <= 10 ^ 9
# 1 <= c <= 10 ^ 9
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            print("bit_a",bit_a)
            bit_b = b & 1
            print("bit b",bit_b)
            bit_c = c & 1
            print("bit c", bit_c)

            if bit_c == 1:
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                flips += bit_a + bit_b

            a >>= 1
            b >>= 1
            c >>= 1

        return flips


# Example usage:
sol = Solution()
print("Outputof one is 1st",sol.minFlips(2, 6, 5))  # Output: 3
# print("Outputof one is 1st",sol.minFlips(4, 2, 7))  # Output: 1
# print("Outputof one is 1st",sol.minFlips(1, 2, 3))  # Output: 0
