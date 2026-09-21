class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            part1 = (left+right)//2
            part2 = (m+n+1)//2 - part1

            if part1 == 0:
                left1 = float("-inf")
            else:
                left1 = nums1[part1-1]

            if part1 == m:
                right1 = float("inf")
            else:
                right1 = nums1[part1]

            if part2 == 0:
                left2 = float("-inf")
            else:
                left2 = nums2[part2-1]

            if part2 == n:
                right2 = float("inf")
            else:
                right2 = nums2[part2]

            if left1<=right2 and left2<=right1:
                # odd no. of elements
                if(m+n)%2 == 1:
                    return max(left1,left2)
                #even no. of elements
                return(
                    max(left1,left2) + min(right1,right2)
                )/2
            elif left1>right2:
                right = part1 - 1
            else:
                left = part1 + 1

                    