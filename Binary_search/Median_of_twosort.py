from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # ensure A is the smaller array
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m  # i is the count of elements taken from A (0..m)
        while True:
            i = (l + r) // 2        # A left size
            j = half - i            # B left size

            Aleft = A[i-1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')
            Bleft = B[j-1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            # correct partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd total -> min of right halves
                if total % 2:
                    return float(min(Aright, Bright))
                # even total -> average of max left and min right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                # we took too many from A, move left
                r = i - 1
            else:
                # we took too few from A, move right
                l = i + 1
