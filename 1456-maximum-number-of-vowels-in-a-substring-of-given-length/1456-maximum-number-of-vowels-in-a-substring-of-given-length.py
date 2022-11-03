class Solution:
    def maxVowels(self, s, k):
        max_vowel=0
        current_num_vowel=0
        arr=[]
        for i in s:
            arr.append(i)
            if i in ['a','e','i','o','u']:
                current_num_vowel +=1
            if len(arr)>k and arr.pop(0) in ['a','e','i','o','u']:
                current_num_vowel -=1
            if current_num_vowel > max_vowel:
                max_vowel = current_num_vowel
                if max_vowel ==k:
                    return max_vowel
        return max_vowel