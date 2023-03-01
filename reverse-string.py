class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reverse(s,1)

    def reverse(self,s,n):
        if n == math.ceil(len(s)/2):
            s[n-1],s[len(s)-n] = s[len(s)-n],s[n-1] 
            return 
        self.reverse(s,n+1)
        s[n-1],s[len(s)-n] = s[len(s)-n],s[n-1] 
        return