class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        dp = [[0]*len(nums2) for i in range(len(nums1))]
        for i in range(len(nums1)):
            dp[i][0] = int(nums1[i] == nums2[0])
            res = max(res,dp[i][0])

        for j in range(len(nums2)):
            dp[0][j] = int(nums1[0] == nums2[j])
            res = max(res,dp[0][j])

        for i in range(1,len(nums1)):
            for j in range(1,len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res,dp[i][j])
        
        
        return res

        



        