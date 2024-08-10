class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        A: 3
        B: 3
            AABABBA
              i
                  j
        Approach 1: Sliding window
         - point at the first character indicating the start of the window with size 1
         - on each iteration move the right pointer by 1 and add it to dictionary to count
           the frequency
        - on each iteration hence we can only convert k character  we need to keep track of
          the minimum frequency
        """

        count = defaultdict(int)
        l = 0
        r = 0
        max_freq = 0
        max_length = 0

        while r < len(s):
            
            count[s[r]] += 1
            max_freq = max(max_freq,count[s[r]])
            window_size = r - l + 1

            if window_size - max_freq > k:
                count[s[l]] -= 1
                l += 1
            else:
                max_length = max(max_length,window_size)

            r += 1

        return max_length