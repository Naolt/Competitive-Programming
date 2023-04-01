class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = defaultdict(int)
        nums = []
        size = len(words)
        length = 0
        for index,word in enumerate(words):
            nums.append((self.findNum(word),index))
        for i in range(size):
            for j in range(i+1,size):
                if (nums[i][0] & nums[j][0]) == 0:
                    length = max(length,len(words[nums[i][1]])*len(words[nums[j][1]]))
        return length

    def findNum(self,word):
        num = 0
        for char in word:
            k = 1
            k <<= (ord(char)-97)
            num |= k
        print(bin(num))
        return num