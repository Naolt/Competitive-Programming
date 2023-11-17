class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numdic = Counter(nums)
        result = []

        for key,value in numdic.items():
            if value > len(nums)//3:
                result.append(key)

        return result
        