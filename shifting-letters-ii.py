class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s)
        shiftPrefix = [0]*(size+1)
        characters = [chr(97+i) for i in range(26)]
        
        # create the array 
        for index,shift in enumerate(shifts):
            if shift[2] == 0:
                shiftPrefix[shift[0]] -= 1
                shiftPrefix[shift[1]+1] += 1
            else:
                shiftPrefix[shift[0]] += 1
                shiftPrefix[shift[1]+1] -= 1

        print(shiftPrefix)
        # for i in range(1,size):
        #     shiftPrefix[i] = shiftPrefix[-1]+shiftPrefix[i]
        shiftPrefix = list(accumulate(shiftPrefix))
        print(shiftPrefix)
        result = ""
        for index,char in enumerate(s):
            newCode = ord(char)-ord("a") + shiftPrefix[index] + 26
            newCode %= 26
            result += chr(newCode+ord('a'))
            # result += characters[(abs(newCode-97))%26]
        return result