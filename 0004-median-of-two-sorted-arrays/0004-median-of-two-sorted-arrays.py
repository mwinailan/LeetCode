class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            A, B = nums2, nums1
        
        totalLength = len(nums1) + len(nums2)
        halfLength = totalLength // 2
        
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2 # mid, aka rightmost index of A partition
            j = halfLength - i - 2
            
            Aleft = A[i] if i in range(len(A)) else float("-inf")
            Aright = A[i+1] if i + 1 in range(len(A)) else float("inf")
            Bleft = B[j] if j in range(len(B)) else float("-inf")
            Bright = B[j+1] if j + 1 in range(len(B)) else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                #odd length
                if totalLength % 2 == 1:
                    return min(Aright, Bright)
                else:
                #even length
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
            
            