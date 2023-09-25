class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0

        size = len(s)
        nums = [0]*size
        
        if int(s[size-1]) != 0:
            nums[-1] = 1
        
        for i in range(size-2,-1,-1):
            print(nums)
            count = nums[i+1] if int(s[i+1]) > 0 and int(s[i]) > 0 else 0
            if int(s[i]) != 0:                
                if int(s[i:i+2]) < 27:
                    if i+2 < size:
                        count += nums[i+2]
                    else:
                        count += 1

            
            nums[i] = count
        
        return nums[0]