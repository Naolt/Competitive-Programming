class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        size1,size2 = len(nums1),len(nums2)
        dic1 = defaultdict(list)
        dic2 = defaultdict(list)

        for index,num in enumerate(nums1):
            dic1[num].append(index)
        for index,num in enumerate(nums2):
            dic2[num].append(index)
        
        # print(dic1,dic2, bisect_right(dic2[2],0))
        @cache
        def dp(i,j):
            print(i,j)
            if i >= size1 or j >= size2:
                return 0
            
            res1,res2,res3 = 0,0,0
            #search num1 num in num2 after j
            num2Index = bisect_left(dic2[nums1[i]],j)
            if num2Index != len(dic2[nums1[i]]):
                res1 = 1 + dp(i+1,dic2[nums1[i]][num2Index]+1)
            
            #search num2 num in num1 after i
            num1Index = bisect_left(dic1[nums2[j]],i)
            if num1Index != len(dic1[nums2[j]]):
                res2 = 1 + dp(dic1[nums2[j]][num1Index]+1,j+1)

            #leave them both
            res3 = dp(i+1,j+1)

            return max(res1,res2,res3)
        
        return dp(0,0)
        # return 0