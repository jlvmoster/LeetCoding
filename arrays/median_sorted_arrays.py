"""
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List


class Solution:

  def find_median_sorted_arrays(self, nums1: List[int],
                                nums2: List[int]) -> float:
    pass


if __name__ == '__main__':
  solution = Solution()
  result = solution.find_median_sorted_arrays([1, 3], [2])
  print(result)
