class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = Counter(nums)
        right = Counter()
        for num in nums:
            if not left[num]: continue
            left[num] -= 1
            if right[num - 1] > 0:
                right[num - 1] -= 1
                right[num] += 1
            elif left[num + 1] and left[num + 2]:
                left[num + 1] -= 1
                left[num + 2] -= 1
                right[num + 2] += 1
            else:
                return False
        return True