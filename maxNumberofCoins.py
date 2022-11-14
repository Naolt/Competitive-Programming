class Solution(object):
	def maxCoins(self, piles):
		piles.sort(reverse=True)
		print(piles)
		max = 0
		
		for i in range(0,len(piles)-int(len(piles)/3),2):
			max+=piles[i+1]
			print(i,piles[i+1])
		
		return max

check = Solution()
print(check.maxCoins([9,8,7,6,5,1,2,3,4]
))
