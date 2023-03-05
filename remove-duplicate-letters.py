class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        letterDict = collections.Counter(s)
        notfinalState = collections.Counter(s)
        for char in s:
            letterDict[char] -= 1
            if not notfinalState[char]:
                continue
            while stack and stack[-1] > char and letterDict[stack[-1]] > 0:
                print("removing",stack[-1],stack,letterDict)
                notfinalState[stack.pop()] = 1
            stack.append(char)
            notfinalState[char] = 0
        return "".join(stack)