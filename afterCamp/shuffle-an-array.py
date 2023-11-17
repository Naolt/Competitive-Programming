class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums
        self.copy = nums[:]

    def reset(self) -> List[int]:
        self.copy = self.ori[:]
        return self.copy

    def shuffle(self) -> List[int]:
        for i in range(len(self.copy)):
            j = random.randint(0,len(self.copy)-1)
            self.copy[i],self.copy[j] = self.copy[j],self.copy[i]

        return self.copy
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()