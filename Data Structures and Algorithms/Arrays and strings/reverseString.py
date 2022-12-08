"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    @staticmethod
    def reverseString(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Two pointers
# Time complexity : O(N) to swap N/2 element.
# Space complexity : O(1)
