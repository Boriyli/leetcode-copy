"""
https://leetcode.com/problems/number-of-1-bits/
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages, such as Java, there is no unsigned integer type.
In this case, the input will be given as a signed integer type. It should not affect your implementation,
as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3, the input represents the signed integer. -3.
"""


class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        pass


if __name__ == '__main__':
    print(Solution.hammingWeight(n=0o0000000000000000000000000001011))
