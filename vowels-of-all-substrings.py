class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(['a','e','i','o','u'])

        result = 0

        for index,char in enumerate(word):
            if char in vowels:
                left = index+1
                right = len(word)-index
                result += (left*right)

        return result