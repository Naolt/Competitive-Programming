class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        

        @cache
        def dp(i,s):
            
            # if (i,s) in memo:
                # return memo[(i,s)]
            if i == len(nums1):
                return 0

            swapped,normal = float('inf'),float('inf')
            
            if i == 0:
                normal = dp(i+1,False)
                if nums1[i] != nums2[i]:
                    nums1[i],nums2[i] = nums2[i],nums1[i]
                    swapped = dp(i+1,True)+1
                    nums2[i],nums1[i] = nums1[i],nums2[i]
            else:
                if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                    normal = dp(i+1,False)
                if nums1[i] != nums2[i] and nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                    nums1[i],nums2[i] = nums2[i],nums1[i]
                    swapped = dp(i+1,True)+1
                    nums2[i],nums1[i] = nums1[i],nums2[i]

            return min(swapped,normal)

        return dp(0,False)