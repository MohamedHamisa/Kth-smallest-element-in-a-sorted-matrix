class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid, count, j = (lo+hi)//2, 0, len(matrix[0])
            for row in matrix:
                while j>=1 and row[j-1] > mid:
                    j -= 1
                count += j
            if count < k:
                lo = mid+1
            else:
                hi = mid
        return lo


