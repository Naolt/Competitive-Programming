class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.getScore(nums,0,len(nums)-1,True)
        if score[0] >= score[1]:
            return True
        return False

    def getScore(self,arr,l,r,p1t):
        
        if l == r:
            if p1t:
                return [arr[l],0]
            else:
                return [0,arr[l]]
        
        if p1t:
            left = self.getScore(arr,l+1,r,not p1t)
            right = self.getScore(arr,l,r-1,not p1t)
            left[0] += arr[l]
            right[0] += arr[r]
            if left[0] >= right[0]:
                return left
            else:
                return right
        else:
            left = self.getScore(arr,l+1,r,not p1t)
            right = self.getScore(arr,l,r-1,not p1t)
            left[1] += arr[l]
            right[1] += arr[r]
            if left[1] > right[1]:
                return left
            else:
                return right